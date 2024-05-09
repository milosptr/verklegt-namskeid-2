from src.models import Company


class CompanyController:
    def __init__(self):
        self.companyService = Company()

    def get_all_companies(self):
        return self.companyService.get_all_companies()
