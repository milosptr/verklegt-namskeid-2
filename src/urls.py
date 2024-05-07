from django.urls import path

<<<<<<< HEAD
from .views.views import home, contact_us

=======
from .views.views import home
from .views.views import about_us
from .views.views import application_guide
from .views.views import companies
>>>>>>> f17498093ef41472b18691215f90621a6eee4486
# This will be our main urls file
# We will include all the urls from the apps here
# Look at it as the main router of the application
# Example url:path('/about', name='about') -> This is the syntax for creating a url

urlpatterns = [
    path('', home, name='home'),
<<<<<<< HEAD
    path('contact_us', contact_us, name='contact_us')
    ]
=======
    path('about-us', about_us, name='about_us'),
    path('application-guide', application_guide, name='application_guide'),
    path('companies', companies, name='companies')
]
>>>>>>> f17498093ef41472b18691215f90621a6eee4486
