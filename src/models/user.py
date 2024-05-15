import string
import random
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.db import models

from src.exceptions.UserExceptions import CreateAccountException
from src.models.application import Application
from src.models.user_skill import UserSkill
from src.models.skill import Skill
from src.models.user_resume import UserResume
from src.models.user_experience import UserExperience
from src.models.user_recommendation import UserRecommendation
from src.models.city import City
from src.models.country import Country


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=255)
    avatar = models.TextField(null=True)
    role = models.IntegerField(default=0)
    about = models.TextField(null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    verified_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(id=id)

    def save(self, *args, **kwargs):
        try:
            user = super(User, self).save(*args, **kwargs)
            # Send out an email to the user
            # here
        except Exception as e:
            raise CreateAccountException(str(e))

    def validate_fields(self, role=0):
        """
        Validate the fields of the model
        :param type: int - 0 for normal user, 1 for business user
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
        if role == 0 and not self.address:
            errors.append('Address is required')
        if role == 0 and not self.city_id:
            errors.append('City is required')
        if role == 0 and not self.country_id:
            errors.append('Country is required')

        return ','.join(errors)

    def validate_business_fields(self, type=0):
        errors = list()
        if type == 0 and not self.company_id:
            errors.append('Company is required')
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

    def parse_logged_in_user(self):
        user_skills = UserSkill.objects.filter(user_id=self.id)
        skills = list()
        for s in user_skills:
            skill = Skill.objects.get(id=s.skill_id)
            skills.append({"id": skill.id, "name": skill.name})

        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.first_name + ' ' + self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'role': self.role,
            'about': self.about,
            'address': self.address,
            'city': City.get_by_id(self.city_id),
            'full_address': self.address + ', ' + self.city.name + ' ' + self.city.zip + ', ' + self.country.name,
            'recommendations': UserRecommendation.objects.filter(user_id=self.id),
            'experiences': UserExperience.objects.filter(user_id=self.id),
            'resume': UserResume.objects.filter(user_id=self.id).first(),
            'skills': skills,
            'country': Country.get_by_id(self.country_id),
            'applications': Application.objects.filter(user_id=self.id),
            'company': self.company,
            'avatar': self.avatar,
            'verified_at': self.verified_at
        }

    @staticmethod
    def generate_password():
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))

    def reset_password(self):
        password = self.generate_password()
        self.password = self.hash_password(password)
        self.save()
        return password

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @classmethod
    def get_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except:
            return None

