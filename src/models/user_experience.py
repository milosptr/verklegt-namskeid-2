from datetime import datetime

from django.db import models


class UserExperience(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField()
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.company} - {self.role}"

    class Meta:
        db_table = 'user_experiences'
        ordering = ['-created_at']
        verbose_name = 'UserExperience'
        verbose_name_plural = 'UserExperiences'
