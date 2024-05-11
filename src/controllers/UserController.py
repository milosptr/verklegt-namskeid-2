from django.contrib.sessions.models import Session
from django.db import IntegrityError
from django.shortcuts import render, redirect

from src.controllers.CityController import CityController
from src.controllers.CountryController import CountryController
from src.exceptions.UserExceptions import CreateAccountException, LoginException
from src.models import User, Company


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
