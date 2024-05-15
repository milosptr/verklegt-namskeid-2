from django.db import models
from django.contrib.auth.models import User

class UserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.link
