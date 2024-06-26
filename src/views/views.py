from django.shortcuts import get_object_or_404

from src.controllers.ApplicationController import ApplicationController
from src.controllers.CategoryController import CategoryController
from src.controllers.CityController import CityController
from src.controllers.CountryController import CountryController
from src.controllers.JobController import JobController
from src.controllers.ProtectedViewController import ProtectedViewController
from src.controllers.CompanyController import CompanyController
from src.models import Company, Job, LikedJob, Application, Type
from src.controllers.EmailController import *
from ..controllers.CategoryController import CategoryController
from ..controllers.TypeController import TypeController

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
    job_offers = JobController().get_all()
    companies = CompanyController().get_all_companies()
    categories = CategoryController().get_categories()
    job_types = Type.get_all()
    selected_types = [int(i) for i in request.GET.getlist('type')]

    if request.GET.get('jobs'):
        job_offers = JobController.filter(request)
    if request.GET.get('q'):
        job_offers = JobController.search(request)

    return GeneralViewController(request).render('pages/home.html', {
        'job_offers': job_offers,
        'job_types': job_types,
        'categories': categories,
        'companies': companies,
        'selected_types': selected_types
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

    job_list = Job.get_by_company(company_id)

    print ("Job List: ",job_list)

    return GeneralViewController(request).render('pages/company_details.html', {
        'company': company,
        'job_list': job_list
    })

def job_offer(request):
    return GeneralViewController(request).render('pages/job_offer.html')


def account_created(request):
    return GeneralViewController(request).render('pages/success/account_created.html')


def report_bug(request):
    return GeneralViewController(request).render('pages/report_bug.html')


def application_submitted(request):
    return GeneralViewController(request).render('pages/application_submitted.html')

############################################################################################################
# Protected views
############################################################################################################
def profile(request):
    countries = CountryController().get_countries()
    cities = CityController().get_all()
    return ProtectedViewController(request).render('pages/account/profile.html',
                                                   {'countries': countries, 'cities': cities})


def employer_dashboard(request):
    countries = CountryController().get_countries()
    cities = CityController().get_all()
    return ProtectedViewController(request).render('pages/employer-dashboard.html')


def make_job_offer(request):
    categories = CategoryController().get_categories()
    types = TypeController().get_types()
    return ProtectedViewController(request).render('pages/make_job_offer.html', {
        'categories': categories,
        'types': types
    })


def application(request, id: int):
    """
        This is the application view that takes two parameters
        id: The id of the job that the application is for
        step: The step of the application
    """
    return ApplicationController().handle_application_view(request, id)


def view_candidate(request):
    return ProtectedViewController(request).render('pages/view_candidate.html')


def edit_job_offer(request, id: int):
    return JobController().edit_job_offer_view(request, id)


def job_offer(request, id:int):
    job = JobController().get_by_id(id)
    return ProtectedViewController(request).render('pages/job_offer.html', {'job': job})


def job_list(request):
    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'pages/job_list.html', {'filter': job_filter})


def employer_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login')

    user = User.get_by_id(user_id)
    if not user or user.role == 0:
        return redirect('/profile')
    return ProtectedViewController(request).render('pages/employer-dashboard.html')

