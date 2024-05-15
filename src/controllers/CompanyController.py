from src.models import Company, Job

class CompanyController:
    def __init__(self):
        self.companyService = Company()

    def get_all_companies(self):
        return self.companyService.get_all()

    def get_jobs_by_company(self, company_id):
        return Job.objects.filter(company_id=company_id)