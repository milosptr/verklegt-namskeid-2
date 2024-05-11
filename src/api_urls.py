from django.urls import path

from src.controllers.UserController import UserController

prefix = 'api/v1'

urlpatterns = [
    path(f'{prefix}/create-account', UserController.create_account_view, name='create_account'),
    path(f'{prefix}/create-business-account', UserController.create_business_account_view, name='create_business_account'),
    path(f'{prefix}/login', UserController.login, name='login'),
    path(f'{prefix}/user/<int:id>/about', UserController.update_about, name='update_about'),
    path(f'{prefix}/user/<int:id>/recommendation', UserController.add_recommendation, name='add_recommendation'),
    path(f'{prefix}/user/<int:id>/experience', UserController.add_experience, name='add_experience'),
    path(f'{prefix}/user/<int:id>/resume', UserController.add_resume, name='add_cv'),
]
