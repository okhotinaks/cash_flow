from django.urls import path

from .views import (FinancialRecordListView,
                    FinancialRecordCreareView,
                    FinancialRecordUpdateView,
                    FinancialRecordDeleteView)

urlpatterns = [
    path('', FinancialRecordListView.as_view(), name='record-list'),
    path('add/', FinancialRecordCreareView.as_view(), name='record-create'),
    path(
        '<int:pk>/edit/',
        FinancialRecordUpdateView.as_view(),
        name='record-edit'
    ),
    path(
        '<int:pk>/delete/',
        FinancialRecordDeleteView.as_view(),
        name='record-delete'
    )
]
