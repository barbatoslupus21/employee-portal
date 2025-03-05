from django.urls import path
from . import views

urlpatterns = [
    path('admin-timelogs/', views.admin_timelogs, name="admin-timelogs"),
    path('timelogs/', views.timelogs, name='timelogs'),
    path('upload-excel/', views.upload_timelogs, name='upload_timelogs'),
    path('api/timelogs/', views.EmployeeTimelogsListView.as_view(), name='timelogs-list'),
]
