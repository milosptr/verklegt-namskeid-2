from datetime import datetime

from django.db import models
from src.models.job import Job 

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=150)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    logo = models.TextField(null=True)
    cover_image = models.TextField(null=True)
    website = models.CharField(max_length=150, null=True)
    jobs = models.ManyToManyField('Job', related_name='companies')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('name')

    def full_address(self):
        return f'{self.address}, {self.city.name} {self.city.zip}, {self.country.name}'

    def get_available_jobs(self):
        return Job.objects.filter(company_id=self.id, status__lt=2)

    def validate_fields(self):
        errors = list()
        if not self.name:
            errors.append('Company name is required')
        if not self.description:
            errors.append('Company description is required')
        if not self.address:
            errors.append('Company address is required')
        if not self.city_id:
            errors.append('Company city is required')
        if not self.country_id:
            errors.append('Company country is required')
        return ','.join(errors)

    class Meta:
        db_table = 'companies'
        ordering = ['-created_at']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
