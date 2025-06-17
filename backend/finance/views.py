from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import (
    FinancialRecord, Category, SubCategory, Status, OperationType
)
from .forms import FinancialRecordForm
from .filters import FinancialRecordFilter


class FinancialRecordListView(ListView):
    """
    Представление для отображения списка записей движения денежных средств(ДДС)
    с возможностью фильтрации и пагинации.
    """
    model = FinancialRecord
    template_name = 'finance/record_list.html'
    context_object_name = 'records'
    paginate_by = 10

    def get_queryset(self):
        """
        Получаем исходный QuetySet записей и применяем фильтрацию
        на основе GET-параметров, используя FinancialRecordFilter.

        Возвращаем отсортированный отфильтрованный список.
        """
        queryset = super().get_queryset().select_related(
            'status', 'operation_type', 'category', 'subcategory'
        )
        self.filterset = FinancialRecordFilter(
            self.request.GET,
            queryset=queryset
        )
        return self.filterset.qs.order_by('-created_at', '-id')

    def get_context_data(self, **kwargs):
        """
        Добавляем в контекст шаблона форму фильтра,
        списки возможных значений фильтров, значения текущих фильтров.
        """
        context = super().get_context_data(**kwargs)

        context['filter'] = self.filterset
        context['statuses'] = Status.objects.all()
        context['operation_types'] = OperationType.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()

        get = self.request.GET
        context['selected_status'] = get.get('status', '')
        context['selected_operation_type'] = get.get('operation_type', '')
        context['selected_category'] = get.get('category', '')
        context['selected_subcategory'] = get.get('subcategory', '')
        context['selected_date'] = get.get('created_at', '')
        return context


class FinancialRecordCreareView(CreateView):
    """Представление для создания записей ДДС."""
    model = FinancialRecord
    form_class = FinancialRecordForm
    template_name = 'finance/record_form.html'
    success_url = reverse_lazy('record-list')


class FinancialRecordUpdateView(UpdateView):
    """Представление для редактирования существующей записи ДДС."""
    model = FinancialRecord
    form_class = FinancialRecordForm
    template_name = 'finance/record_form.html'
    success_url = reverse_lazy('record-list')


class FinancialRecordDeleteView(DeleteView):
    """Представление для удаления записи ДДС с подтверждением действия."""
    model = FinancialRecord
    template_name = 'finance/record_delete.html'
    success_url = reverse_lazy('record-list')
