from django import forms

from .models import FinancialRecord, Category, SubCategory


class FinancialRecordForm(forms.ModelForm):
    """Форма для создания и редактирования записей ДДС."""

    class Meta:
        model = FinancialRecord
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        """
        Переопределение конструктора формы:
        - фильтрация категорий в зависимости от выбранного типа операции,
        - фильтрация подкатегорий в зависимости от выбранной категории.
        """

        super().__init__(*args, **kwargs)

        data = self.data or None
        instance = self.instance if self.instance.pk else None

        # Фильтрация категорий по выбранному типу операции
        operation_type_id = (
            int(data.get('operation_type'))
            if data and data.get('operation_type') else
            instance.operation_type_id if instance else None
        )
        if operation_type_id:
            self.fields['category'].queryset = Category.objects.filter(
                operation_type_id=operation_type_id
            )

        # Фильтрация подкатегорий по выбранной категории
        category_id = (
            int(data.get('category'))
            if data and data.get('category') else
            instance.category_id if instance else None
        )
        if category_id:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(
                category_id=category_id
            )

    def clean(self):
        """"
        Общая валидация на соответствие тип-категория/категория-подкатегория.
        """
        cleaned_data = super().clean()
        operation_type = cleaned_data.get('operation_type')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        if (
            category and operation_type and
            category.operation_type != operation_type
        ):
            self.add_error(
                'category',
                'Категория не относится к выбранному типу операции.'
            )

        if subcategory and category and subcategory.category != category:
            self.add_error(
                'subcategory',
                'Подкатегория не принадлежит выбранной категории.'
            )
