from django.shortcuts import render, redirect, get_object_or_404

from src.business.application import ApplicationLogic
from src.controllers.ApplicationController import ApplicationController
from src.controllers.CityController import CityController
from src.controllers.CountryController import CountryController
from src.controllers.GeneralViewController import GeneralViewController
from src.controllers.JobController import JobController
from src.controllers.ProtectedViewController import ProtectedViewController
from src.exceptions import ApplicationException
from src.exceptions.ApplicationException import ApplicationSubmitted
from src.controllers.CompanyController import CompanyController
from src.models import Company, Job
from src.controllers.EmailController import *
from src.controllers.CategoryController import CategoryController
from ..filters import JobFilter

# Views are the functions that handle the requests from the user
# You can think of them as the controller in the MVC pattern
# They are responsible for processing the request and returning the response
# All the views are connected to the urls.py file in the same folder

############################################################################################################
# Account views
############################################################################################################
def log_in(request):
    if request.session.get('is_authenticated'):
        return redirect('/profile')
    return render(request, 'pages/account/login.html')


def log_out(request):
    request.session.flush()
    return render(request, 'pages/account/login.html')


def create_account(request):
    if request.session.get('is_authenticated'):
        return redirect('/profile')
    return render(request, 'pages/create_account.html')


def forgot_password(request):
    return render(request, 'pages/forgot-password.html')


############################################################################################################
# General views
############################################################################################################
def home(request):
    """
    This is the home view or the index page of the application
    """
    category_id = request.GET.get('category')
    company_id = request.GET.get('company_filter')

    if category_id and category_id != '1':
        job_offers = JobController().get_by_category(category_id)
    elif company_id and company_id != '1':
        job_offers = CompanyController().get_jobs_by_company(company_id)
    else:
        job_offers = JobController().get_all()

    companies_list = CompanyController().get_all_companies()
    category_list = CategoryController().get_categories()
    filters = request.GET
    print(filters.get('category'))
    print(filters.get('company_filter'))

    return GeneralViewController(request).render('pages/home.html', {
        'job_offers': job_offers, 
        'companies_list': companies_list, 
        'category_list': category_list
    })


def contact_us(request):
    """
    This is the contact us view
    """
    return GeneralViewController(request).render('pages/contact_us.html')


def about_us(request):
    return GeneralViewController(request).render('pages/about_us.html')


def application_guide(request):
    return GeneralViewController(request).render('pages/application_guide.html')


def companies(request):
    query = request.GET.get('q')
    if query:
        companies_list = Company.objects.filter(name__icontains=query).order_by('name')
    else:
        companies_list = CompanyController().get_all_companies()
    return GeneralViewController(request).render('pages/companies.html', {'companies_list': companies_list})


def not_found(request):
    return GeneralViewController(request).render('pages/404.html')


def application_guide(request):
    return GeneralViewController(request).render('pages/application_guide.html')


def company_profile(request, company_name):
    company = get_object_or_404(Company, name=company_name)
    return GeneralViewController(request).render('pages/company_profile.html', {'company': company})


def company_details(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return GeneralViewController(request).render('pages/company_details.html', {'company': company})


def job_offer(request):
    return GeneralViewController(request).render('pages/job_offer.html')


def account_created(request):
    return GeneralViewController(request).render('pages/success/account_created.html')


def report_bug(request):
    return GeneralViewController(request).render('pages/report_bug.html')

############################################################################################################
# Protected views
############################################################################################################
def profile(request):
    countries = CountryController().get_countries()
    cities = CityController().get_all()
    return ProtectedViewController(request).render('pages/account/profile.html',
                                                   {'countries': countries, 'cities': cities})


def employer_dashboard(request):
    return ProtectedViewController(request).render('pages/employer-dashboard.html')


def make_job_offer(request):
    return ProtectedViewController(request).render('pages/make_job_offer.html')


def application(request, id: int, step: int):
    """
        This is the application view that takes two parameters
        id: The id of the job that the application is for
        step: The step of the application
    """
    return ApplicationController().handle_application_view(request, id, step)


def make_job_offer(request):
    return ProtectedViewController(request).render('pages/make_job_offer.html')


def view_candidate(request):
    return ProtectedViewController(request).render('pages/view_candidate.html')


def edit_job_offer(request):
    return ProtectedViewController(request).render('pages/edit_job_offer.html')


def job_offer(request, id:int):
    job = JobController().get_by_id(id)
    return ProtectedViewController(request).render('pages/job_offer.html', {'job': job})

def job_list(request):
    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'pages/job_list.html', {'filter': job_filter})

def employer_dashboard(request):
    return ProtectedViewController(request).render('pages/employer-dashboard.html')

