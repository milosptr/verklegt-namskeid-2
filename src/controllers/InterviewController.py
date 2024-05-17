from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import redirect

from src.models.job import Job
from src.models.interview import Interview


class InterviewController:
    def __init__(self):
        self.interview_service = Interview()

    def get_by_user(self, user_id: int):
        return self.interview_service.get_by_user(user_id)

    @staticmethod
    def invite_candidate(request, job_id: int, user_id: int):
        if request.method != 'POST':
            return redirect('/not-found')

        try:
            job = Job.get_by_id(job_id)
            if not job:
                return redirect('/not-found')

            interview = Interview(
                company_id=job.company_id,
                job_id=job_id,
                user_id=user_id,
                status=0,
                interview_date=datetime.now() + timedelta(days=7),  # Interview date is set to 7 days from now
                location=job.company.full_address()
            )
            interview.save()
            return redirect(f'/employer-dashboard')

        except Exception as e:
            return redirect('/not-found')

    @staticmethod
    def update_interview_status(request, job_id: int, user_id: int):
        try:
            job = Job.get_by_id(job_id)
            if not job:
                return redirect('/not-found')

            interview = Interview.get_by_job_user(job_id, user_id)
            if not interview:
                return redirect('/not-found')
            action = request.POST.get('action')
            if action == 'complete':
                interview.status = 3

            interview.save()

            return redirect(f'/employer-dashboard')
        except Exception as e:
            print(f'Error: {e}')
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('/employer-dashboard')

    @staticmethod
    def update_status(request, id: int):
        try:
            interview = Interview.get_by_id(id)
            if not interview:
                return redirect('/not-found')
            action = request.POST.get('action')
            if action == 'accept':
                interview.status = 1
            elif action == 'reject':
                interview.status = 2
            elif action == 'complete':
                interview.status = 3

            interview.save()

            if request.user.role == 0:
                return redirect(f'/employer-dashboard')
            return redirect(f'/profile')
        except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('/profile')



