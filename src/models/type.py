from datetime import datetime

from django.db import models


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
      return cls.objects.all().order_by('name')

    class Meta:
        db_table = 'types'
        ordering = ['-created_at']
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
