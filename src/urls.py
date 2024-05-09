from django.urls import path, re_path
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
from .views.views import application
from .views.views import not_found
from .views.views import company_profile
from .views.views import company_details
from .views.views import creating_business_account_info
from .views.views import make_job_offer
from .views.views import job_offer
# This will be our main urls file
# We will include all the urls from the apps here
# Look at it as the main router of the application
# Example url:path('/about', name='about') -> This is the syntax for creating a url

urlpatterns = [
    path('', home, name='home'),
    path('contact-us', contact_us, name='contact_us'),
    path('about-us', about_us, name='about_us'),
    path('application-guide', application_guide, name='application_guide'),
    path('companies', companies, name='companies'),
    path('company-profile', company_profile, name='company_profile'),
    path('log-in', log_in, name='log_in'),
    path('create-account', create_account, name='create_account'),
    path('create-account-info', create_account_info, name='create_account_info'),
    path('profile', profile, name='profile'),
    path('companies', companies, name='companies'),
    path('company-details', company_details, name='company_details'),
    path('creating-business-account-info',creating_business_account_info, name="creating_business_account_info"),
    path('make-job-offer', make_job_offer, name='make_job_offer'),
    path('job-offer', job_offer, name='job_offer'),
    path('companies', companies, name='companies'),
    path('application/<int:id>/<int:step>', application, name='application'),
    re_path(r'.*', not_found, name='not_found')  # This is a catch-all url that leads to a 404 page
]
