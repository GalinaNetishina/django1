from django_filters import rest_framework as filters, DateTimeFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateTimeFromToRangeFilter()
    creator = filters.CharFilter(field_name='creator', lookup_expr='exact')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']
