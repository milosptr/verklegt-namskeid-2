from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'types'
        ordering = ['-created_at']
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
