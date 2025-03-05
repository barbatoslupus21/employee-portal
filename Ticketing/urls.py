from django.urls import path
from . import views

urlpatterns = [
    
    path('mis-ticket/', views.user_ticket, name='ticket'),
    path('submit-ticket/', views.submit_ticket, name="submit-ticket"),
    path('device/', views.user_device, name="user-devices"),
    path('edit-device/<str:pk>/', views.edit_device, name='edit-user-device'),
    path('delete-device/<str:pk>/', views.delete_device, name='delete-device'),
    path('create-device/', views.create_device, name='create-device'),

    path('admin-ticket/', views.admin_ticket, name="admin-ticket"),
    path('submit-diagnosis/<str:pk>/', views.submit_diagnosis, name="submit-diagnosis"),
    path('export-tickets/', views.export_tickets, name="export-ticket"),
    path('admin-device/', views.admin_device, name="admin-devices"),
    path('export-device-ticket/<str:pk>/', views.export_device_tickets, name="export-device-ticket"),
]
