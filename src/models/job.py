from datetime import datetime

from django.db import models
from django.utils import timezone


class Job(models.Model):
    STATUS = [
        (0, 'Active'),
        (1, 'Interviewing'),
        (2, 'Closed')
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.IntegerField(default=0, choices=STATUS)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    types = models.ManyToManyField('Type', related_name='jobs')
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    @classmethod
    def get_by_id(cls, job_id):
        return cls.objects.get(id=job_id)

    @classmethod
    def get_by_category(cls, job_category_id):
        return cls.objects.filter(category_id=job_category_id)

    @classmethod
    def get_by_company(cls, company_id):
        return cls.objects.filter(company_id=company_id)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def remaining_days(self):
        now = timezone.now()
        delta = self.due_date - now
        if delta.days > 0:
            return f"Ends in {delta.days} days"
        elif delta.days == 0:
            return "Ends today"
        else:
            return "Ended"


    def get_all_jobs(self):
        return self.objects.all()


    def validate_fields(self):
        errors = list()

        if not self.title:
            errors.append("Job title is required")
        if not self.description:
            errors.append("Job description is required")
        if not self.category:
            errors.append("Job category is required")
        if not self.company:
            errors.append("Job is required to belong to company")
        if not self.status:
            errors.append("Job status is required")
        if not self.types:
            errors.append("Job has to have a type")

    def get_job_types(self):
        try:
            return self.types.all()
        except:
            return []
        

    def get_status(self):
        if self.status == 0:
            return 'Active'
        elif self.status == 1:
            return 'Interviewing'
        elif self.status == 2:
            return 'Closed'

    class Meta:
        db_table = 'jobs'
        ordering = ['-created_at']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
