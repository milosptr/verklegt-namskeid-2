from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect

from src.controllers.JobController import JobController
from src.controllers.ProtectedViewController import ProtectedViewController
from src.models import Application, User


class ApplicationController:

    @staticmethod
    def handle_application_view(request, id: int):
        try:
            job = JobController().get_by_id(id)
            if not job:
                return redirect('/not-found')

            if request.method == 'GET':
                return ProtectedViewController(request).render('pages/application.html', {
                    'job': job,
                })

            if request.method != 'POST':
                return redirect('/not-found')

            if not request.POST.get('cover_letter'):
                message = 'Cover letter is required'
                messages.error(request, message)
                return redirect(f'/application/{id}')

            if request.POST.get('cover_letter') and len(request.POST.get('cover_letter')) < 100:
                message = 'Cover has to be at least 100 character long'
                messages.error(request, message)
                return redirect(f'/application/{id}')

            user = User().get_by_id(request.POST.get('key'))
            if not user:
                message = 'Sorry, we could not find your account. Please try again later.'
                messages.error(request, message)
                return redirect(f'/application/{id}')

            application = Application(
                user_id=user.id,
                job_id=id,
                cover_letter=request.POST.get('cover_letter'),
                status=0,
                submission_date=datetime.now()
            )
            application.save()

            return redirect('/application-submitted')

        # This is a catch-all exception handler
        # because I really don't care about the exception
        # you should never end up here, but if you do then 404 :)
        except Exception as e:
            print(f'Exception: {str(e)}')
            return redirect('/not-found')
