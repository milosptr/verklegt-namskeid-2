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
