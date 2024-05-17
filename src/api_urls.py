from django.urls import path

from src.controllers.CompanyController import CompanyController
from src.controllers.InterviewController import InterviewController
from src.controllers.JobController import JobController
from src.controllers.UserController import UserController
from src.controllers.EmailController import EmailController
from src.controllers.ApplicationController import ApplicationController

prefix = 'api/v1'

urlpatterns = [
    path(f'{prefix}/create-account', UserController.create_account_view, name='create_account'),
    path(f'{prefix}/create-business-account', UserController.create_business_account_view, name='create_business_account'),
    path(f'{prefix}/login', UserController.login, name='login'),
    path(f'{prefix}/reset-password', EmailController.reset_password, name='reset_password'),

    # Company routes
    path(f'{prefix}/company/<int:id>/update-info', CompanyController.upload_info, name='upload_info'),
    path(f'{prefix}/company/<int:id>/logo', CompanyController.upload_logo, name='upload_logo'),
    path(f'{prefix}/company/<int:id>/cover', CompanyController.upload_cover, name='upload_cover'),

    # Interview routes
    path(f'{prefix}/invite-candidate/<int:job_id>/<int:user_id>', InterviewController.invite_candidate, name='invite_candidate'),
    path(f'{prefix}/invite-candidate/<int:job_id>/<int:user_id>/status', InterviewController.update_interview_status, name='update_interview_status'),
    path(f'{prefix}/interview/<int:id>/status', InterviewController.update_status, name='update_status'),

    # Job routes
    path(f'{prefix}/job/create', JobController.create_job, name='create_job'),
    path(f'{prefix}/job/<int:id>/status', JobController().update_status, name='update_status'),
    path(f'{prefix}/job/<int:id>/update-job', JobController().update_job, name='update_job'),

    # Application routes
    path(f'{prefix}/view-candidate/<int:id>', ApplicationController().view_candidate, name='view_candidate'),
    path(f'{prefix}/application/<int:id>/review', ApplicationController().review_application, name='review_application'),

    # User routes
    path(f'{prefix}/user/<int:id>/like/<int:job>', UserController.like_job, name='like_job'),
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
