from django.urls import path, re_path

from .controllers.UserController import UserController
from .views.views import home, account_created
from .views.views import about_us
from .views.views import application_guide
from .views.views import create_account
from .views.views import profile
from .views.views import log_in, log_out
from .views.views import companies
from .views.views import application
from .views.views import not_found
from .views.views import company_profile
from .views.views import company_details
from .views.views import contact_us
from .views.views import make_job_offer
from .views.views import job_offer
from .views.views import employer_dashboard

# This will be our main urls file
# We will include all the urls from the apps here
# Look at it as the main router of the application
# Example url:path('/about', name='about') -> This is the syntax for creating the url

urlpatterns = [
    # Account views
    path('login', log_in, name='log_in'),
    path('logout', log_out, name='log_out'),
    path('create-account', create_account, name='create_account'),
    path('create-personal-account', UserController.create_account_view, name='create-personal-account'),
    path('create-business-account', UserController.create_business_account_view, name='create-business-account'),
    path('account-created', account_created, name='account_created'),

    # General views
    path('', home, name='home'),
    path('about-us', about_us, name='about_us'),
    path('application-guide', application_guide, name='application_guide'),
    path('contact-us', contact_us, name='contact_us'),
    path('companies', companies, name='companies'),
    path('company-details/<int:company_id>/', company_details, name='company_details'),
    path('make-job-offer', make_job_offer, name='ma'
                                                'ke_job_offer'),
    path('job-offer', job_offer, name='job_offer'),

    # Protected views
    path('profile', profile, name='profile'),
    path('job-offer/<int:job_id>', job_offer, name='job_offer'),
    path('companies', companies, name='companies'),
    path('application/<int:id>/<int:step>', application, name='application'),
    path('employer-dashboard', employer_dashboard, name='employer_dashboard'),
    path('company-profile', company_profile, name='company_profile'),
    path('make-job-offer', make_job_offer, name='make_job_offer'),
    path('application/<int:id>/<int:step>', application, name='application'),

    re_path(r'.*', not_found, name='not_found')  # This is a catch-all url that leads to a 404 page
]
