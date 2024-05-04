from django.db import models


class UserExperience(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.company}) - {self.role}"

    class Meta:
        db_table = 'user_experiences'
        ordering = ['-created_at']
        verbose_name = 'UserExperience'
        verbose_name_plural = 'UserExperiences'
