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
        return self.objects.all()

    class Meta:
        db_table = 'companies'
        ordering = ['-created_at']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
