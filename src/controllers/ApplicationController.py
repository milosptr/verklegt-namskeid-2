from django.shortcuts import render, redirect

from src.controllers.ProtectedViewController import ProtectedViewController
from src.exceptions.ApplicationException import ApplicationSubmitted, ApplicationException


class ApplicationController:
    def __init__(self):
        pass

    def handle_application_view(self, request, id, step):
        if step < 1 or step > 5:
            return redirect('/not-found')

        if request.method == 'GET':
            return ProtectedViewController(request).render('pages/application.html', {'id': id, 'step': step})

        if request.POST != 'POST':
            return redirect('/not-found')

        try:
            # Check if the request is a POST request and if the application step was handled successfully
            if self.handle_application_step(step, dict(request.POST.items())):
                step += 1
                # Move to the next step
                return redirect(f'/application/{id}/{step}')

            # Render the application page with the id and step
            return ProtectedViewController(request).render('pages/application.html', {'id': id, 'step': step})
        except ApplicationSubmitted:
            # If the application was submitted successfully, return a success page
            return render(request, 'pages/application_submitted.html')
        except ApplicationException as e:
            print(f'Error: {e}')
            return redirect('/not-found')

    def handle_application_step(self, step: int, data: dict):
        if step == 1:
            return self.handle_user_info(data)
        if step == 2:
            return self.handle_user_experience(data)
        if step == 3:
            return self.handle_user_recommendation(data)
        if step == 4:
            return self.handle_user_cover_letter(data)
        if step == 5:
            return self.handle_application(data)
        raise ApplicationException('Invalid step')

    def handle_user_info(self, data: dict):
        print(f'Handling user info: {data}')
        return True

    def handle_user_experience(self, data: dict):
        print(f'Handling user experience: {data}')
        return True

    def handle_user_recommendation(self, data: dict):
        print(f'Handling user recommendation: {data}')
        return True

    def handle_user_cover_letter(self, data: dict):
        print(f'Handling user cover letter: {data}')
        return True

    def handle_application(self, data: dict):
        print(f'Handling application: {data}')
        raise ApplicationSubmitted('Application submitted successfully')
