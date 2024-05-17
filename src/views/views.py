from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
#from src.business.application import ApplicationLogic
from django.shortcuts import get_object_or_404

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
from src.models import Company, Job, LikedJob, Application, Category
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
    job_offers = JobController().get_all()
    companies_list = CompanyController().get_all_companies()
    categories_list = CategoryController().get_categories()

    filters = request.GET
    if filters and filters.get('liked'):
        liked_jobs = LikedJob.objects.filter(user_id=request.session.get('user_id'))
        job_offers = [liked_job.job for liked_job in liked_jobs]

    if filters and filters.get('applied'):
        applications = Application.get_by_user(request.session.get('user_id'))
        job_offers = [a.job for a in applications]

    if filters and filters.get('company'):
        company_id = filters.get('company')
        job_offers = Job.get_by_company(company_id)

    if filters and filters.get('order_by'):
        order_by = filters.get('order_by') == 'asc' if '' else '-'
        job_offers = job_offers.order_by(f'{order_by}due_date')

    if filters and filters.get('category'):
        job_category_id = filters.get('category')
        job_offers = Job.get_by_category(job_category_id)

    return GeneralViewController(request).render('pages/home.html', {
        'job_offers': job_offers,
        'companies_list': companies_list,
        'categories_list': categories_list,
        'company_filter': filters.get('company'),
        'category_filter': filters.get('category'),
        'order_filter': filters.get('order_by')
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

def create_job_offer(request):
    print("hello?")
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        print("Received title:", title)
        print("Received category ID:", category_id)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, "Selected category does not exist.")
            return redirect('make_job_offer')  # Redirect back to form page
        start_date = request.POST.get('start_date')
        print("Received start_date:", start_date)
        due_date = request.POST.get('due_date')
        print("Received due_date:", due_date)
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, "Selected category does not exist.")
            return redirect('make_job_offer')
        print("HEY I AM HERE!")
        try:
            job = Job.objects.create(
                title=title,
                category=category,
                start_date=start_date,
                due_date=due_date,
                description=description
            )
            print("HELLO")
            messages.success(request, "Job created successfully!")
            return redirect('job_list')  # Redirect to job listing
        except Exception as e:
            messages.error(request, str(e))
            return redirect('make_job_offer')
    categories_list = Category.objects.all()
    return render(request, 'make_job_offer.html')

def employer_dashboard(request):
    countries = CountryController().get_countries()
    cities = CityController().get_all()
    return ProtectedViewController(request).render('pages/employer-dashboard.html')


def make_job_offer(request):
    if request.method == 'POST':
        # Assuming form data is sent as POST request
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        address = request.POST.get('address')

        # Create a new Job instance and save it
        job = Job(
            title=title,
            address=address,
            description=description,
            category_id=category_id,
            start_date=start_date,
            due_date=due_date,
            company=request.user.company  # Assuming the user is linked to a company
        )
        try:
            job.save()
            messages.success(request, "Job offer created successfully!")
            return redirect('some_view_name')  # Redirect after POST to avoid resubmitting the form
        except Exception as e:
            messages.error(request, f"Failed to create job offer: {str(e)}")

    # Handle GET request
    categories_list = CategoryController().get_categories()
    return render(request, 'pages/make_job_offer.html', {'categories_list': categories_list})


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

