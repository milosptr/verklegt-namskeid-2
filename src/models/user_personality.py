from datetime import datetime

from django.db import models


class UserPersonality(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'user_personalities'
        ordering = ['-created_at']
        verbose_name = 'UserPersonality'
        verbose_name_plural = 'UserPersonalities'
