from django.shortcuts import render

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

def about_us(request):
    return render(request, 'pages/about_us.html')

def application_guide(request):
    return render(request, 'pages/application_guide.html')

def companies(request):
    return render(request, 'pages/companies.html')

def company_profile(request):
    return render(request, 'pages/company_details.html')

def company_details(request):
    return render(request, 'pages/company_details.html')

def creating_account(request):
    return render(request, 'pages/creating_account.html')
    return render(request, 'pages/company_profile.html')

def company_details(request):
    return render(request, 'pages/company_details.html')
