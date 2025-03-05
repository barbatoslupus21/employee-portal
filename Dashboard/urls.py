from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('Dashboard', views.user_dashboard, name='Dashboard'),
    path('Dashboard-admin', views.admin_dashboard, name='admin-dashboard'),
    path('weather/', views.weather_view, name='weather_view'),
]
