from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        ordering = ['-created_at']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
