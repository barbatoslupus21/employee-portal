from django.urls import path
from . import views

urlpatterns = [
    
    path('api/notifications/', views.get_notifications_api, name='get_notifications_api'),
    path('api/notifications/<int:notification_id>/mark-seen/', 
         views.mark_notification_as_seen, 
         name='mark_notification_as_seen'),
]
