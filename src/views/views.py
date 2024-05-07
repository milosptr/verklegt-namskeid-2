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

# Do this for all views that you need to create
# And then create the templates in the templates folder

def about_us(request):
    return render(request, 'pages/about_us.html')

def application_guide(request):
    return render(request, 'pages/application_guide.html')

def log_in(request):
    return render(request, 'pages/log_in.html')

def companies(request):
    return render(request, 'pages/companies.html')