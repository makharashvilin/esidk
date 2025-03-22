from datetime import date, timedelta
import django_filters
from .models import Item



class ItemFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    in_stock = django_filters.BooleanFilter(method='instock', label='in stock')
    preordered = django_filters.BooleanFilter(method='preordered', label='preordered')
    near_expiry = django_filters.BooleanFilter(method='near_expiry', label='near expiry date')





    def instock(self, queryset, name, value):
        queryset = queryset.filter(stock_qty__gt=0)
        return queryset


    def preordered(self, queryset, name, value):
        queryset = queryset.filter(stock_qty__lt=0)
        return queryset


    def near_expiry(self, queryset, name, value):
        queryset = queryset.filter(expiration_date__range=(date.today(), date.today()+timedelta(days=4)))
        return queryset




    class Meta:
        model = Item
        fields = ['name', 'description', 'in_stock', 'preordered', 'near_expiry']