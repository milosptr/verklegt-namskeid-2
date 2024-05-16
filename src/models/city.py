from datetime import datetime

from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    class Meta:
        db_table = 'cities'
        ordering = ['-created_at']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
