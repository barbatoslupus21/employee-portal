from django.urls import path
from . import views

urlpatterns = [
    
    path('prf/', views.prf_view, name='user-prf'),
    path('submit-prf/', views.submit_prf, name='submit-prf'),
    path('edit-prf/<str:pk>/', views.edit_prf, name='edit-prf'),
    path('cancel-prf/<str:pk>/', views.cancel_prf, name='cancel-prf'),
    path('admin-prf/', views.admin_prf, name='admin-prf'),
    path('prf/<int:pk>/approve/', views.update_prf_status, {'action': 'approve'}, name='approve-prf'),
    path('prf/<int:pk>/disapprove/', views.update_prf_status, {'action': 'disapprove'}, name='disapprove-prf'),
    path('export-prf/', views.export_prf, name='export-prf'),
]
