from django.db import models
from django.core.validators import MinValueValidator

from datetime import date


class FinanceBaseModel(models.Model):
    """Абстрактная базовая модель."""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Status(FinanceBaseModel):
    """Модель для статуса."""
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class OperationType(FinanceBaseModel):
    """Модель для типа операции."""

    class Meta:
        verbose_name = 'Тип операции'
        verbose_name_plural = 'Типы операций'


class Category(FinanceBaseModel):
    """Модель для категории."""
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='Тип операции'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'operation_type'],
                name='type_category_unique'
            )
        ]


class SubCategory(FinanceBaseModel):
    """Модель для подкатегории."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category'],
                name='category_subcategory_unique'
            )
        ]


class FinancialRecord(models.Model):
    """Модель для записи ДДС."""
    created_at = models.DateField(
        default=date.today,
        verbose_name='Дата создания'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name='Статус'
    )
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
        verbose_name='Тип операции'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        verbose_name='Подкатегория'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Сумма в рублях',
        validators=[MinValueValidator(1, 'Минимальная сумма в рублях - 1')]
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name='Комментарий'
        )

    class Meta:
        verbose_name = 'Запись ДДС'
        verbose_name_plural = 'Записи ДДС'
        constraints = [
            models.UniqueConstraint(
                fields=['created_at', 'status', 'operation_type', 'category', 'subcategory', 'amount'],
                name='unique_financial_record_combination'
            )
        ]