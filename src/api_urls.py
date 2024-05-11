from django.urls import path

from src.controllers.UserController import UserController
prefix = f'api/v1'

urlpatterns = [
    path(f'{prefix}/create-account', UserController.create_account_view, name='create_account'),
    path(f'{prefix}/create-business-account', UserController.create_business_account_view, name='create_business_account'),
    path(f'{prefix}/login', UserController.login, name='login'),
    path(f'{prefix}/user/<int:id>/about', UserController.update_about, name='update_about'),
]
