import django_filters
from .models import Tour, Category

class TourFilter(django_filters.FilterSet):
    start_time = django_filters.DateFilter(field_name='start_time', lookup_expr='gte')
    cost = django_filters.NumberFilter(field_name='cost', lookup_expr='gte')
    place_name = django_filters.CharFilter(field_name='place_name', lookup_expr='icontains')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Tour
        fields = ['start_time', 'cost', 'place_name', 'category']