from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'skills'
        ordering = ['-created_at']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
