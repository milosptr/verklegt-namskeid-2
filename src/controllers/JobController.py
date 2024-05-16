from src.models import Job


class JobController:
    def __init__(self):
        self.job_service = Job()

    def get_all(self):
        return self.job_service.get_all()

    def get_by_id(self, job_id):
        return self.job_service.get_by_id(job_id)
    
    def get_by_category(self, job_category_id):
        return Job.objects.filter(category_id=job_category_id)
    
    def get_by_company(self, company_id):
        return Job.get_by_company(company_id)