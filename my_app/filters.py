from . import models
import django_filters

class PersonFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    # email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = models.Person
        fields = ['name']