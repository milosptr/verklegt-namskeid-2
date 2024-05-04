from django.db import models


class Application(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.IntegerField(default=0)
    submission_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.job) + ' - ' + str(self.user)

    class Meta:
        db_table = 'applications'
        ordering = ['-created_at']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
