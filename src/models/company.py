from datetime import datetime

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=150)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    logo = models.TextField(null=True)
    cover_image = models.TextField(null=True)
    website = models.CharField(max_length=150, null=True)
    jobs = models.ManyToManyField('Job', related_name='companies')
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


    def get_all_companies(self):
        return Company.objects.all()
      
    @classmethod
    def get_all(cls):
        return cls.objects.all()

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
