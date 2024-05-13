import base64

from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db import IntegrityError
from django.shortcuts import render, redirect

from src.controllers.CityController import CityController
from src.controllers.CountryController import CountryController
from src.controllers.ProtectedViewController import ProtectedViewController
from src.exceptions.UserExceptions import CreateAccountException, LoginException
from src.models import User, Company, UserRecommendation, UserExperience, UserResume, Skill, UserSkill


class UserController:
    @staticmethod
    def logout(request):
        # clear the user's session data
        Session.objects.filter(session_key=request.session.session_key).delete()
        return redirect('/')

    @staticmethod
    def login(request):
        """
        Handles incoming requests to login a user
        """
        if request.method != 'POST':
            return render(request, 'pages/404.html')

        try:
            user = User.objects.get(email=request.POST.get('email'))
            if not user.verify_password(request.POST.get('password'), user.password):
                raise LoginException('Invalid email or password')
            request.session['is_authenticated'] = True
            request.session['user_id'] = user.id
            request.session.save()

        except User.DoesNotExist:
            return render(request, 'pages/account/login.html', {'errors': ['Invalid email or password']})
        except LoginException as e:
            return render(request, 'pages/account/login.html', {'errors': [str(e)]})
        except Exception as e:
            return render(request, 'pages/account/login.html', {'errors': [str(e)]})

        # If everything goes well, redirect to profile page
        return redirect('/profile')

    @staticmethod
    def create_account_view(request):
        """
        Handles incoming requests to create an account
        """
        countries = CountryController().get_countries()
        cities = CityController().get_all()

        if request.method == 'GET':
            return render(request, 'pages/account/create_account.html', {'countries': countries, 'cities': cities})

        if request.method != 'POST':
            return render(request, 'pages/404.html')

        try:
            UserController().create_account(dict(request.POST.items()))
        except CreateAccountException as e:
            errors = str(e).split(',')
            context = dict(request.POST.items())
            return render(request, 'pages/account/create_account.html',
                          {'countries': countries, 'cities': cities, 'errors': errors, 'context': context})
        except Exception as e:
            return render(request, 'pages/account/create_account.html',
                          {'countries': countries, 'cities': cities, 'errors': [str(e)]})

        # If everything goes well, redirect to success page
        return redirect('/account-created')

    @staticmethod
    def create_business_account_view(request):
        companies = Company().get_all()
        countries = CountryController().get_countries()
        cities = CityController().get_all()

        if request.method == 'GET':
            return render(request, 'pages/account/create_business_account.html', {'companies': companies, 'countries': countries, 'cities': cities})
        if request.method != 'POST':
            return render(request, 'pages/404.html')

        try:
            UserController().create_business_account(dict(request.POST.items()))
        except CreateAccountException as e:
            errors = str(e).split(',')
            context = dict(request.POST.items())
            return render(request, 'pages/account/create_business_account.html',
                          {'companies': companies, 'countries': countries, 'cities': cities, 'errors': errors, 'context': context})
        except Exception as e:
            return render(request, 'pages/account/create_business_account.html',
                          {'companies': companies, 'countries': countries, 'cities': cities, 'errors': [str(e)]})

        # If everything goes well, redirect to success page
        return redirect('/account-created')

    @staticmethod
    def create_account(data: dict):
        try:
            if not data and not data.get('password'):
                raise CreateAccountException('Password is required')

            hashed_password = User.hash_password(data.get('password'))

            user = User(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                password=hashed_password,
                phone_number=data.get('phone_number'),
            )

            if user.validate_fields():
                raise CreateAccountException(user.validate_fields())

            # Save the user if everything is okay
            user.save()

        except IntegrityError as e:
            if 'unique constraint' in str(e):
                # since we know that the email is the only unique field
                # we can safely assume that the email already exists
                raise CreateAccountException('Email already exists')
            raise CreateAccountException('Something went wrong! Please try again')
        except Exception as e:
            raise CreateAccountException(str(e))

    @staticmethod
    def create_business_account(data: dict):
        try:
            if not data and not data.get('password'):
                raise CreateAccountException('Password is required')

            hashed_password = User.hash_password(data.get('password'))

            user = User(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                password=hashed_password,
                phone_number=data.get('phone_number'),
                address=data.get('address'),
                city=data.get('city'),
                country=data.get('country'),
                role=1  # Business user
            )

            if user.validate_fields(role=1):
                raise CreateAccountException(user.validate_fields(role=1))

            if data.get('company_type') == 'existing':
                validation = user.validate_business_fields(data.get('company_type'))
                if validation:
                    raise CreateAccountException(validation)
                user.company_id = data.get('company_id')
            if data.get('company_type') == 'custom':
                company = Company(
                    name=data.get('company_name'),
                    description=data.get('company_description'),
                    address=data.get('company_address'),
                    city_id=data.get('city_id'),
                    country_id=data.get('country_id'),
                )
                validation = company.validate_fields()
                if validation:
                    raise CreateAccountException(validation)
                company.save()
                user.company_id = company.id

            # Save the user if everything is okay
            user.save()

        except IntegrityError as e:
            if 'unique constraint' in str(e):
                # since we know that the email is the only unique field
                # we can safely assume that the email already exists
                raise CreateAccountException('Email already exists')
            raise CreateAccountException('Something went wrong! Please try again')
        except Exception as e:
            raise CreateAccountException(str(e))

    @staticmethod
    def update_info(request, id: int):
        user = User.get_by_id(id)
        if not user:
            return render(request, 'pages/404.html')
        if request.method == 'GET':
            return redirect('/profile')
        if request.method != 'POST':
            return render(request, 'pages/404.html')
        try:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.address = request.POST.get('address')
            user.city_id = request.POST.get('city_id')
            user.country_id = request.POST.get('country_id')
            user.save()
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')
        return redirect('/profile')

    @staticmethod
    def update_about(request, id: int):
        user = User.get_by_id(id)
        if not user:
            return render(request, 'pages/404.html')
        if request.method == 'GET':
            return redirect('/profile')
        if request.method != 'POST':
            return render(request, 'pages/404.html')
        try:
            user.about = request.POST.get('about')
            user.save()
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')
        return redirect('/profile')

    @staticmethod
    def add_recommendation(request, id: int):
        if request.method != 'POST':
            return render(request, 'pages/404.html')

        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')
            recommendation = UserRecommendation(
                user_id=user.id,
                company=request.POST.get('company'),
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                position=request.POST.get('position')
            )
            recommendation.save()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')

    @staticmethod
    def add_experience(request, id: int):
        if request.method != 'POST':
            return render(request, 'pages/404.html')
        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')

            still_working = request.POST.get('still_working')
            end_date = request.POST.get('end_date')
            if still_working:
                end_date = None

            experience = UserExperience(
                user_id=user.id,
                description=request.POST.get('description'),
                company=request.POST.get('company'),
                role=request.POST.get('role'),
                start_date=request.POST.get('start_date'),
                end_date=end_date
            )
            experience.save()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')

    @staticmethod
    def add_resume(request, id: int):
        if request.method != 'POST':
            return render(request, 'pages/404.html')
        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')
            resume = UserResume.objects.filter(user_id=user.id).first()
            if resume:
                resume.content = request.POST.get('resume')
                resume.save()
            else:
                resume = UserResume(
                    user_id=user.id,
                    content=request.POST.get('resume')
                )
                resume.save()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')

    @staticmethod
    def add_skill(request, id: int):
        if request.method != 'POST':
            return render(request, 'pages/404.html')
        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')
            data = dict(request.POST.items())
            for key in data.keys():
                if key.startswith('skill_'):
                    skill_id = key.replace('skill_', '')
                    skill = Skill.objects.get(id=skill_id)
                    if not skill:
                        continue

                    user_skill = UserSkill(
                        user_id=user.id,
                        skill=skill,
                        level=5  # for now hardcode the level to 5
                    )
                    user_skill.save()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')

    @staticmethod
    def remove_skill(request, id: int, skill: int):
        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')
            user_skill = UserSkill.objects.filter(user_id=user.id, skill_id=skill).first()
            if user_skill:
                user_skill.delete()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')

    @staticmethod
    def upload_avatar(request, id: int):
        if request.method != 'POST':
            return render(request, 'pages/404.html')

        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')
            avatar = request.FILES['avatar']
            if not avatar:
                return ProtectedViewController(request).render('pages/account/profile.html', {'errors': ['Avatar image is required']})

            # Read the binary data from the image
            image_data = avatar.read()

            # Encode the binary data to base64
            encoded_image = base64.b64encode(image_data)

            # Store the base64-encoded data as a string in the database
            user.avatar = 'data:image/png;base64,' + encoded_image.decode('utf-8')
            user.save()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')

    @staticmethod
    def remove_experience(request, id: int, experience: int):
        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')
            user_experience = UserExperience.objects.filter(user_id=user.id, id=experience).first()
            if user_experience:
                user_experience.delete()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')

    @staticmethod
    def remove_recommendation(request, id: int, recommendation: int):
        try:
            user = User.get_by_id(id)
            if not user:
                return render(request, 'pages/404.html')
            user_recommendation = UserRecommendation.objects.filter(user_id=user.id, id=recommendation).first()
            if user_recommendation:
                user_recommendation.delete()
            return redirect('/profile')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('profile')
