from datetime import datetime

from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=20)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name: str):
        short = name.split(' ')
        short = ''.join([s[0] for s in short])
        return cls.objects.create(name=name, short=short)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        db_table = 'category'
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
