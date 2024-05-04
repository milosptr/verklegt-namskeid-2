from django.db import models


class LikedJob(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''

    class Meta:
        db_table = 'liked_jobs'
        ordering = ['-created_at']
        verbose_name = 'LikedJob'
        verbose_name_plural = 'LikedJobs'
