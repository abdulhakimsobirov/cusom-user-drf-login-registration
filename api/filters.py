from django_filters.rest_framework import FilterSet, filters
from .models import Group, Sms

class GroupFilter(FilterSet):
    created_at_gt = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_lt = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Group
        fields = ['id', 'name']


class SmsFilter(FilterSet):
    created_at_gt = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_lt = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Sms
        fields = ['id', 'group']
