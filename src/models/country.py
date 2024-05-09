from datetime import datetime

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        db_table = 'countries'
        ordering = ['-created_at']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
