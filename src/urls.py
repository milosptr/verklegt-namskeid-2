from django.urls import path

from .views.views import home, contact_us

# This will be our main urls file
# We will include all the urls from the apps here
# Look at it as the main router of the application
# Example url:path('/about', home, name='about') -> This is the syntax for creating a url

urlpatterns = [
    path('', home, name='home'),
    path('contact_us', contact_us, name='contact_us')
    ]
