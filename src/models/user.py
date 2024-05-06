from datetime import datetime

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    avatar = models.TextField()
    role = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    verified_at = models.DateTimeField()
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

