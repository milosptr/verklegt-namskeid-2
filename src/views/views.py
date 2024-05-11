from django.shortcuts import render, redirect, get_object_or_404

from src.business.application import ApplicationLogic
from src.controllers.CountryController import CountryController
from src.controllers.GeneralViewController import GeneralViewController
from src.controllers.ProtectedViewController import ProtectedViewController
from src.exceptions import ApplicationException
from src.exceptions.ApplicationException import ApplicationSubmitted
from src.controllers.CompanyController import CompanyController
from src.models import Company


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

############################################################################################################
# General views
############################################################################################################
def home(request):
    """
    This is the home view or the index page of the application
    """
    return GeneralViewController(request).render('pages/home.html')


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


############################################################################################################
# Protected views
############################################################################################################
def profile(request):
    return ProtectedViewController(request).render('pages/profile.html')


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
    # Check if the step is valid, if not return a 404 page
    if step < 1 or step > 5:
        return render(request, 'pages/404.html')

    try:
        # Check if the request is a POST request and if the application step was handled successfully
        if request.POST and ApplicationLogic().handle_application_step(step, dict(request.POST.items())):
            step += 1
            # Move to the next step
            return redirect(f'/application/{id}/{step}')

        # Render the application page with the id and step
        return render(request, 'pages/application.html', {'id': id, 'step': step})
    except ApplicationSubmitted:
        # If the application was submitted successfully, return a success page
        return render(request, 'pages/application_submitted.html')
    except ApplicationException as e:
        print(f'Error: {e}')
        return render(request, 'pages/404.html')


def make_job_offer(request):
    return render(request, 'pages/make_job_offer.html')


def creating_account(request):
    return render(request, 'pages/creating_account.html')


def job_offer(request):
    return render(request, 'pages/job_offer.html')


def employer_dashboard(request):
    return render(request, 'pages/employer-dashboard.html')


def account_created(request):
    return render(request, 'pages/success/account_created.html')

def edit_profile_info(request):
    return render(request, 'pages/edit_profile_info.html')

def report_bug(request):
    return render(request, 'pages/report_bug.html')
