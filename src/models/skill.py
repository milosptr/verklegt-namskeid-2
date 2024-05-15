from datetime import datetime

from django.db import models


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'skills'
        ordering = ['-created_at']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
