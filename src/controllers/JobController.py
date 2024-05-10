from src.models import Job


class JobController:
    def __init__(self):
        self.jobService = Job()

    def get_all_jobs(self):
        return self.jobService.get_all_jobs()
