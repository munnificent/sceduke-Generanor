# api/urls.py

from django.urls import path
from .views import ScheduleCreateView, ScheduleDetailView

urlpatterns = [
    path('schedules/', ScheduleCreateView.as_view(), name='schedule-create'),
    path('schedules/<uuid:unique_link>/', ScheduleDetailView.as_view(), name='schedule-detail'),
]
