from datetime import datetime

from django.db import models


class LikedJob(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return ''

    @classmethod
    def get_by_user(cls, user_id):
        return cls.objects.filter(user_id=user_id)

    @classmethod
    def get_by_job(cls, job_id):
        return cls.objects.filter(job_id=job_id)

    @classmethod
    def get_by_user_and_job(cls, user_id, job_id):
        return cls.objects.filter(user_id=user_id, job_id=job_id)

    class Meta:
        db_table = 'liked_jobs'
        ordering = ['-created_at']
        verbose_name = 'LikedJob'
        verbose_name_plural = 'LikedJobs'
