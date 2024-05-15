from django.db import models


class Interview(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Accepted'),
        (2, 'Rejected'),
        (3, 'Completed')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    interview_date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Interview on {self.interview_date} for {self.user} at {self.company}"

    class Meta:
        db_table = 'interviews'
        ordering = ['-created_at']
        verbose_name = 'Interview'
        verbose_name_plural = 'Interviews'

