import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    company = django_filters.CharFilter(field_name='company__name', lookup_expr='iexact')
    ordering = django_filters.OrderingFilter(
        fields=[
            ('category__name', 'category'),
            ('company__name', 'company'),
            ('start_date', 'start_date'),
            ('due_date', 'due_date'),
            ('created_at', 'created_at'),
        ],
        field_labels={
            'category__name': 'Job Category',
            'company__name': 'Company',
            'start_date': 'Start Date',
            'due_date': 'Due Date',
            'created_at': 'Created At',
        }
    )
   
   
   
    class Meta:
        model = Job
        fields = ['category', 'company']