from django.urls import path
from .views import MonthlySummaryView

urlpatterns = [
    path('reports/monthly-summary/', MonthlySummaryView.as_view(), name='monthly-summary'),
]
