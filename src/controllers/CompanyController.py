import base64

from django.shortcuts import redirect

from src.controllers.ProtectedViewController import ProtectedViewController
from src.models import Company, Job

class CompanyController:
    def __init__(self):
        self.companyService = Company()

    def get_all_companies(self):
        return self.companyService.get_all()

    def get_jobs_by_company(self, company_id):
        return Job.objects.filter(company_id=company_id)
    
    def get_all_available_jobs(self):
        return Job.objec

    @staticmethod
    def upload_info(request, id):
        if request.method != 'POST':
            return redirect('/not-found')

        try:
            company = Company.objects.get(id=id)
            if not company:
                return ProtectedViewController(request).render('pages/account/profile.html', {'errors': ['Company not found']})

            company.name = request.POST['name']
            company.description = request.POST['description']
            company.website = request.POST['website']
            company.address = request.POST['address']
            company.city_id = request.POST['city_id']
            company.country_id = request.POST['country_id']
            company.save()

            return redirect('/profile')
        except Exception as e:
            return ProtectedViewController(request).render('pages/account/profile.html', {'errors': [str(e)]})

    @staticmethod
    def upload_logo(request, id):
        if request.method != 'POST':
            return redirect('/not-found')

        try:
            company = Company.objects.get(id=id)
            if not company:
                return ProtectedViewController(request).render('pages/account/profile.html', {'errors': ['Company not found']})

            logo = request.FILES['logo']
            if not logo:
                return ProtectedViewController(request).render('pages/account/profile.html', {'errors': ['Logo image is required']})

            # Read the binary data from the image
            image_data = logo.read()

            # Encode the binary data to base64
            encoded_image = base64.b64encode(image_data)

            company.logo = f'data:image/png;base64,{encoded_image.decode("utf-8")}'
            company.save()
            return redirect('/profile')
        except Exception as e:
            return ProtectedViewController(request).render('pages/account/profile.html', {'errors': [str(e)]})

    @staticmethod
    def upload_cover(request, id):
        if request.method != 'POST':
            return redirect('/not-found')

        try:
            company = Company.objects.get(id=id)
            if not company:
                return ProtectedViewController(request).render('pages/account/profile.html', {'errors': ['Company not found']})

            cover = request.FILES['cover']
            if not cover:
                return ProtectedViewController(request).render('pages/account/profile.html', {'errors': ['Cover image is required']})

            # Read the binary data from the image
            image_data = cover.read()

            # Encode the binary data to base64
            encoded_image = base64.b64encode(image_data)

            company.cover_image = f'data:image/png;base64,{encoded_image.decode("utf-8")}'
            company.save()
            return redirect('/profile')
        except Exception as e:
            return ProtectedViewController(request).render('pages/account/profile.html', {'errors': [str(e)]})
