from django.urls import path

from src.controllers.UserController import UserController
prefix = f'api/v1'

urlpatterns = [
    path(f'{prefix}/create-account', UserController.create_account_view, name='create_account'),
]
