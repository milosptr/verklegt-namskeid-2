from django.shortcuts import render, redirect

from src.business.application import ApplicationLogic
from src.exceptions import ApplicationException
from src.exceptions.ApplicationException import ApplicationSubmitted


# Views are the functions that handle the requests from the user
# You can think of them as the controller in the MVC pattern
# They are responsible for processing the request and returning the response
# All the views are connected to the urls.py file in the same folder

def home(request):
    """
    This is the home view or the index page of the application
    """
    return render(request, 'pages/home.html')


def contact_us(request):
    """
    This is the contact us view
    """
    return render(request, 'pages/contact_us.html')


# Do this for all views that you need to create
# And then create the templates in the templates folder

def about_us(request):
    return render(request, 'pages/about_us.html')


def application_guide(request):
    return render(request, 'pages/application_guide.html')


def log_in(request):
    return render(request, 'pages/log_in.html')


def create_account(request):
    return render(request, 'pages/create_account.html')


def create_account_info(request):
    return render(request, 'pages/create_account_info.html')


def profile(request):
    return render(request, 'pages/profile.html')


def companies(request):
    return render(request, 'pages/companies.html')


def not_found(request):
    return render(request, 'pages/404.html')


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

def about_us(request):
    return render(request, 'pages/about_us.html')


def application_guide(request):
    return render(request, 'pages/application_guide.html')


def companies(request):
    return render(request, 'pages/companies.html')


def company_profile(request):
    return render(request, 'pages/company_profile.html')

def company_details(request):
    return render(request, 'pages/company_details.html')

def creating_business_account_info(request):
    return render(request, 'pages/creating_business_account_info.html')

def make_job_offer(request):
    return render(request, 'pages/make_job_offer.html')

def creating_account(request):
    return render(request, 'pages/creating_account.html')
    return render(request, 'pages/company_profile.html')

def job_offer(request):
    return render(request, 'pages/job_offer.html')

def employer_dashboard(request):
    return render(request, 'pages/employer-dashboard.html')