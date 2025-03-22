from datetime import date, timedelta
import django_filters
from .models import PurchaseOrder, PurchaseOrderItem



class PurchaseOrderFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderItemFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'




