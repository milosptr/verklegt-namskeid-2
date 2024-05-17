from django.contrib import messages
from django.shortcuts import redirect

from src.controllers.CategoryController import CategoryController
from src.controllers.ProtectedViewController import ProtectedViewController
from src.controllers.TypeController import TypeController
from src.models import Job, LikedJob


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
            job.save()
            return redirect(f'/edit-job-offer/{id}')
        except Exception as e:
            messages.error(request, f'An error occurred while updating job status: {str(e)}')
            return redirect(f'/edit-job-offer/{id}')


    @staticmethod
    def filter(request):
        query_set = Job.objects.all()

        jobs = request.GET.get('jobs')
        if jobs:
            if jobs == '1':
                query_set = Job.objects.all()
            elif jobs == '2':
                job_ids = LikedJob.objects.filter(user=request.session.get('user_id')).values_list('job_id', flat=True)
                query_set = Job.objects.filter(id__in=job_ids)
            elif jobs == '3':
                query_set = Job.objects.filter(application__user_id=request.session.get('user_id')).distinct()
            else:
                query_set = Job.objects.all()

        types = request.GET.getlist('type')
        if types:
            query_set = query_set.filter(types__id__in=types).distinct()

        category = request.GET.get('category')
        if category:
            query_set = query_set.filter(category__id=category)

        company = request.GET.get('company')
        if company:
            query_set = query_set.filter(company__id=company)

        order_by = request.GET.get('order_by', 'created_at')

        if order_by == 'oldest':
            order_by = 'created_at'
        elif order_by == 'newest':
            order_by = '-created_at'
        else:
            order_by = 'created_at'

        query_set = query_set.order_by(order_by)

        return query_set

    @staticmethod
    def search(request):
        query = request.GET.get('q')
        if query:
            return Job.objects.filter(title__icontains=query).order_by('title') | Job.objects.filter(
                description__icontains=query).order_by('title')
        return Job.objects.all()
