from django.urls import path

from src.controllers.UserController import UserController
from src.controllers.EmailController import EmailController

prefix = 'api/v1'

urlpatterns = [
    path(f'{prefix}/create-account', UserController.create_account_view, name='create_account'),
    path(f'{prefix}/create-business-account', UserController.create_business_account_view, name='create_business_account'),
    path(f'{prefix}/login', UserController.login, name='login'),

    # User routes
    path(f'{prefix}/user/<int:id>/about', UserController.update_about, name='update_about'),
    path(f'{prefix}/user/<int:id>/recommendation', UserController.add_recommendation, name='add_recommendation'),
    path(f'{prefix}/user/<int:id>/experience', UserController.add_experience, name='add_experience'),
    path(f'{prefix}/user/<int:id>/resume', UserController.add_resume, name='add_cv'),
    path(f'{prefix}/user/<int:id>/skills', UserController.add_skill, name='add_skill'),
    path(f'{prefix}/user/<int:id>/avatar', UserController.upload_avatar, name='upload_avatar'),
    path(f'{prefix}/user/<int:id>/update-info', UserController.update_info, name='update_info'),
    path(f'{prefix}/user/<int:id>/remove-skill/<int:skill>', UserController.remove_skill, name='remove_skill'),
    path(f'{prefix}/user/<int:id>/remove-experience/<int:experience>', UserController.remove_experience, name='remove_experience'),
    path(f'{prefix}/user/<int:id>/remove-recommendation/<int:recommendation>', UserController.remove_recommendation, name='remove_recommendation'),

    # Contact us
     path(f'{prefix}/contact-us', EmailController.contact_us, name="contact_us")
]
