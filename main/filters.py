import django_filters
from . import models

class TourFilter(django_filters.FilterSet):
    start_time = django_filters.DateFilter(field_name='start_time', lookup_expr='gte')
    cost = django_filters.NumberFilter(field_name='cost', lookup_expr='gte')
    place_name = django_filters.CharFilter(field_name='place_name', lookup_expr='icontains')
    category = django_filters.ModelChoiceFilter(queryset=models.Category.objects.all())

    class Meta:
        model = models.Tour
        fields = ['start_time', 'cost', 'place_name', 'category']


class BookingFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='exact')
    tour = django_filters.CharFilter(field_name='tour__pk', lookup_expr='exact')
    status = django_filters.NumberFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = models.Booking
        fields = ['created_at', 'tour', 'status']