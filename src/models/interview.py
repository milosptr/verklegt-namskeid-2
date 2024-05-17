from django.db import models


class Interview(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Accepted'),
        (2, 'Rejected'),
        (3, 'Completed')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    interview_date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Interview on {self.interview_date} for {self.user} at {self.company} ({self.get_status()})"

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_by_user(cls, user_id):
        return cls.objects.filter(user_id=user_id)

    @classmethod
    def get_by_job_user(cls, job_id, user_id):
        return cls.objects.get(job_id=job_id, user_id=user_id)

    @classmethod
    def get_by_company(cls, company_id):
        return cls.objects.filter(company_id=company_id)

    @classmethod
    def get_by_user_company(cls, user_id, company_id):
        return cls.objects.filter(user_id=user_id, company_id=company_id)

    def get_status(self):
        return self.STATUS_CHOICES[self.status][1]

    def get_status_for_company(self):
        if self.status == 0:
            return 'Pending'
        if self.status == 1:
            return 'Candidate Accepted'
        if self.status == 2:
            return 'Candidate Rejected'
        if self.status == 3:
            return 'Completed'

    class Meta:
        db_table = 'interviews'
        ordering = ['-created_at']
        verbose_name = 'Interview'
        verbose_name_plural = 'Interviews'

