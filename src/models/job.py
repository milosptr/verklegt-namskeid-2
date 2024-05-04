from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    types = models.ManyToManyField('Type', related_name='jobs')
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'jobs'
        ordering = ['-created_at']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
