from datetime import datetime

from django.db import models


class UserResume(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'user_resumes'
        ordering = ['-created_at']
        verbose_name = 'UserResume'
        verbose_name_plural = 'UserResumes'
