import profile

from django.urls import path


from .views.views import home, contact_us

from .views.views import home
from .views.views import about_us
from .views.views import application_guide
from .views.views import create_account
from .views.views import create_account_info
from .views.views import profile
from .views.views import log_in
from .views.views import companies
from .views.views import company_profile
from .views.views import company_details
from .views.views import creating_business_account_info

# This will be our main urls file
# We will include all the urls from the apps here
# Look at it as the main router of the application
# Example url:path('/about', name='about') -> This is the syntax for creating a url

urlpatterns = [
    path('', home, name='home'),
    path('contact_us', contact_us, name='contact_us'),
    path('about-us', about_us, name='about_us'),
    path('application-guide', application_guide, name='application_guide'),
    path('companies', companies, name='companies'),
    path('company-profile', company_profile, name='company_profile'),
    path('log-in', log_in, name='log_in'),
    path('create_account', create_account, name='create_account'),
    path('create_account_info', create_account_info, name='create_account_info'),
    path('profile', profile, name='profile'),
    path('companies', companies, name='companies'),
    path('company-details', company_details, name='company_details'),
    path('creating-business-account-info',creating_business_account_info, name="creating_business_account_info"),
]
