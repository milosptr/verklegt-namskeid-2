from datetime import datetime

from django.db import models


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.IntegerField(default=0)
    submission_date = models.DateTimeField( default=datetime.now)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.job) + ' - ' + str(self.user)

    class Meta:
        db_table = 'applications'
        ordering = ['-created_at']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
