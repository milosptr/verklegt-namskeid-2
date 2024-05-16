from datetime import datetime

from django.db import models


class UserSkill(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    level = models.IntegerField()
    created_at = models.DateTimeField( default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.skill} - {self.level}"

    class Meta:
        db_table = 'user_skills'
        ordering = ['-created_at']
        verbose_name = 'UserSkill'
        verbose_name_plural = 'UserSkills'
