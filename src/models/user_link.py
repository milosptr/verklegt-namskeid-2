from django.db import models
from django.contrib.auth.models import User

class UserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.user.username}: {self.link}"

