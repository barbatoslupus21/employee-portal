from django.urls import path
from . import views

urlpatterns = [
    
    path('announcements/', views.announcement_view, name='announcements'),
    path('create-announcement/', views.create_announcement, name="create-announcement"),
    path('delete-announcement/<str:pk>/', views.delete_announcement, name='delete-announcement'),
]
