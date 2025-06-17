from django.contrib import admin

from .models import (
    Status, OperationType, Category,
    SubCategory, FinancialRecord
)
from .forms import FinancialRecordForm


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Класс для представления модели Status в админ зоне."""
    search_fields = ['name']
    list_display = ['name']


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    """Класс для представления модели OperationType в админ зоне."""
    search_fields = ['name']
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для представления модели Category в админ зоне."""
    search_fields = ['name']
    list_display = ['name', 'operation_type']
    list_filter = ['operation_type']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Класс для представления модели SubCategory в админ зоне."""
    search_fields = ['name']
    list_display = ['name', 'category', 'get_operation_type']
    list_filter = ['category']

    @admin.display(description='Тип операции')
    def get_operation_type(self, obj):
        return obj.category.operation_type


@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    """Класс для представления модели FinancialRecord в админ зоне."""

    form = FinancialRecordForm

    list_display = [
        'created_at', 'status', 'operation_type',
        'category', 'subcategory', 'amount', 'comment'
    ]
    list_filter = [
        'created_at', 'status', 'operation_type',
        'category', 'subcategory'
    ]
    autocomplete_fields = [
        'status', 'operation_type', 'category', 'subcategory'
    ]
    date_hierarchy = 'created_at'
