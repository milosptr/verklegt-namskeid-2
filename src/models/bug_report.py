from django.db import models


class BugReport(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bug_reports'
        ordering = ['-created_at']
        verbose_name = 'BugReport'
        verbose_name_plural = 'BugReports'