from django.db import models


class UserSkill(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.skill} - {self.level}"

    class Meta:
        db_table = 'user_skills'
        ordering = ['-created_at']
        verbose_name = 'UserSkill'
        verbose_name_plural = 'UserSkills'
