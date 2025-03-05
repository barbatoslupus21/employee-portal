from django.urls import path
from . import views

urlpatterns = [
    
    path('feedback', views.feedback_view, name='feedback'),
    path('submit-feedback', views.submit_feedback, name='submit-feedback'),
    path('admin-feedback', views.admin_feedback, name='admin-feedback'),
    path('export-feedback', views.export_feedback, name='export'),
]
