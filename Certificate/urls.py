from django.urls import path
from . import views

urlpatterns = [
    
    path('admin-certificate/', views.admin_certificate, name='admin-certificate'),
    path('create-certificate/', views.create_certificate, name="create-certificate"),
    path('delete-certificate/<str:pk>/', views.delete_certificate, name="delete-certificate"),
    path('view-awardees/<str:pk>/', views.awardees_view, name="awardees"),
    path('delete-awardee/<str:pk>/', views.delete_awardee, name="delete-awardee"),

    path('certificate/', views.certificate_view, name='certificate'),
    path('send-certificate/', views.send_certificate, name='send_certificate'),
]
