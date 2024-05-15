from datetime import datetime

from django.db import models


class UserRecommendation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, null=True, default=None)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.company} ({self.position})"

    class Meta:
        db_table = 'user_recommendations'
        ordering = ['-created_at']
        verbose_name = 'UserRecommendation'
        verbose_name_plural = 'UserRecommendations'
