from datetime import datetime

from django.db import models


class Application(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Reviewed'),
        (2, 'Rejected'),
        (3, 'Accepted')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    submission_date = models.DateTimeField( default=datetime.now)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.job) + ' - ' + str(self.user)

    @classmethod
    def get_by_user(cls, user_id):
        return cls.objects.filter(user_id=user_id).filter(job__status__lt=2)

    @classmethod
    def get_by_company(cls, company_id):
        return cls.objects.filter(job__company_id=company_id).filter(job__status__lt=2)

    @classmethod
    def get_by_category(cls, job_category_id):
        return cls.objects.filter(job__category_id=job_category_id).filter(job__status__lt=2)

    def get_status(self):
        if self.status == 0:
            return 'Pending'
        elif self.status == 1:
            return 'Reviewed'
        elif self.status == 2:
            return 'Rejected'
        else:
            return 'Accepted'

    def get_status_class(self):
        if self.status == 0:
            return 'bg-blue-500'
        elif self.status == 1:
            return 'bg-yellow-500'
        elif self.status == 2:
            return 'bg-red-500'
        else:
            return 'bg-green-500'

    class Meta:
        db_table = 'applications'
        ordering = ['-created_at']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
