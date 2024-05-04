from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
