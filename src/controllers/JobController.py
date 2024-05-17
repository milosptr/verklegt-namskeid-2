from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect

from src.controllers.CategoryController import CategoryController
from src.controllers.ProtectedViewController import ProtectedViewController
from src.controllers.TypeController import TypeController
from src.models import Job, User


class JobController:
    def __init__(self):
        self.job_service = Job()

    def edit_job_offer_view(self, request, id):
        job = self.get_by_id(id)
        categories = CategoryController().get_categories()
        types = TypeController().get_types()
        if not job:
            return redirect('/not-found')
        return ProtectedViewController(request).render('pages/edit_job_offer.html', {
            'job': job,
            'categories': categories,
            'types': types
        })

    def get_all(self):
        return self.job_service.get_all()

    def get_active(self):
        return self.job_service.get_active()

    def get_by_id(self, job_id):
        return self.job_service.get_by_id(job_id)

    def get_by_category(self, job_category_id):
        return Job.objects.filter(category_id=job_category_id)

    def get_by_company(self, company_id):
        return Job.get_by_company(company_id)

    def update_job(self, request, id):
        if request.POST.get('action') == 'delete':
            post = request.POST.copy()
            post['status'] = "2"
            request.POST = post
            return self.update_status(request, id)
        if request.POST.get('action') == 'update':
            job = self.get_by_id(id)
            if not job:
                return redirect('/not-found')
            job.title = request.POST.get('title')
            job.description = request.POST.get('description')
            job.category_id = request.POST.get('category_id')
            job.start_date = request.POST.get('start_date')
            job.due_date = request.POST.get('due_date')

            job.save()

            # Update job types
            job.types.clear()
            types = request.POST.getlist('types')
            for t in types:
                job.types.add(t)

            return redirect(f'/edit-job-offer/{id}')
        return redirect(f'/edit-job-offer/{id}')

    @staticmethod
    def create_job(request):
        if request.method != 'POST':
            return redirect('/not-found')

        try:
            user = User().get_by_id(request.session.get('user_id'))
            if not user:
                messages.error(request, 'User not found')
                return redirect('/make-job-offer')
            category_id = request.POST.get('category_id')
            if request.POST.get('new_job_category'):
                category = CategoryController().create_category(request.POST.get('new_job_category'))
                category_id = category.id

            job = Job(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                category_id=category_id,
                company_id=user.company.id,
                start_date=request.POST.get('start_date'),
                due_date=request.POST.get('due_date')
            )
            job.save()

            # Update job types
            job.types.clear()
            types = request.POST.getlist('types')
            for t in types:
                job.types.add(t)

            return redirect('/employer-dashboard')
        except Exception as e:
            messages.error(request, f'An error occurred while creating job: {str(e)}')
            return redirect('/make-job-offer')

    def update_status(self, request, id):
        try:
            job = self.get_by_id(id)
            if not job:
                return redirect('/not-found')
            status = request.POST.get('status')
            if int(status) < 0 or int(status) > 2:
                messages.error(request, 'Status is required')
                return redirect(f'/edit-job-offer/{id}')
            job.status = int(status)
            if job.status == 2:
                job.updated_at = datetime.now()
            job.save()
            return redirect(f'/edit-job-offer/{id}')
        except Exception as e:
            messages.error(request, f'An error occurred while updating job status: {str(e)}')
            return redirect(f'/edit-job-offer/{id}')
