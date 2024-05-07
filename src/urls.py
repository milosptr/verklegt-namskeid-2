from django.urls import path

from .views.views import home
from .views.views import about_us
from .views.views import application_guide
from .views.views import log_in
from .views.views import companies
# This will be our main urls file
# We will include all the urls from the apps here
# Look at it as the main router of the application
# Example url:path('/about', name='about') -> This is the syntax for creating a url

urlpatterns = [
    path('', home, name='home'),
    path('about-us', about_us, name='about_us'),
    path('application-guide', application_guide, name='application_guide'),
    path('log-in', log_in, name='log_in'),
    path('companies', companies, name='companies')
]
