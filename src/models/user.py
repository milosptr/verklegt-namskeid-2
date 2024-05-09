from datetime import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.db import models

from src.exceptions.UserExceptions import CreateAccountException


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=255)
    avatar = models.TextField(null=True)
    role = models.IntegerField(default=0)
    address = models.CharField(max_length=255, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    verified_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        try:
            user = super(User, self).save(*args, **kwargs)
            # Send out an email to the user
            # here
        except Exception as e:
            raise CreateAccountException(str(e))

    def validate_fields(self):
        """
        Validate the fields of the model
        :return: str
        """
        errors = list()

        if not self.first_name or not self.last_name:
            errors.append('Your name is required')
        if not self.email:
            errors.append('Email is required')
        if not self.password:
            errors.append('Password is required')
        if self.password and len(self.password) < 8:
            errors.append('Password must be at least 8 characters long')
        if self.phone_number and (len(self.phone_number) < 7 or len(self.phone_number) > 15):
            errors.append('Phone number is invalid')
        if not self.address:
            errors.append('Address is required')

        return ','.join(errors)

    @staticmethod
    def hash_password(password):
        """
        Hash the password
        :param password: str
        :return: str
        """
        return make_password(password)

    @staticmethod
    def verify_password(password, hashed_password):
        """
        Verify the password
        :param password: str
        :param hashed_password: str
        :return: bool
        """
        return check_password(password, hashed_password)

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

