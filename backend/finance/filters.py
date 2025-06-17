from django_filters import rest_framework as filters

from .models import FinancialRecord


class FinancialRecordFilter(filters.FilterSet):
    """Фильтр для модели записи движения денежных средств."""
    created_at = filters.DateFilter(label='Дата')

    class Meta:
        model = FinancialRecord
        fields = [
            'created_at', 'status', 'operation_type',
            'category', 'subcategory'
        ]
