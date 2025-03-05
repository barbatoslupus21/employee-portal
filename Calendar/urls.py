from django.urls import path
from . import views

urlpatterns = [
    
    path('admin-calendar/', views.admin_calendar_view, name='admin-calendar'),
    path('calendar/', views.calendar_view, name="calendar"),
    path('submit-event/', views.submit_event, name="submit-event"),
    path('edit-event/<str:pk>/', views.edit_event, name='edit-event'),
    path('delete-event/<str:pk>/', views.event_delete, name='delete-event'),
    path('api/events/', views.event_list, name='event-api'),
]
