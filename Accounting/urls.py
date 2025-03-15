from django.urls import path
from . import views

urlpatterns = [
    
    path('loan-view', views.admin_finance, name='admin-finance'),
    path('loan&allowances/<str:pk>/',views.admin_loan_allowances, name='loan-allowances'),
    path('perfect-attendance/', views.import_perfect_attendance, name='import-attendance'),
    path('medicine/', views.import_medicine, name="import-medicine"),
    path('loan/', views.import_loans, name='import-loans'),
    path('savings/', views.import_savings, name='import-savings'),
    path('payslip-view', views.payslip_view, name="payslip"),
    path('employee-payslip-view/<int:pk>/', views.admin_payslip_view, name="payslip-view"),
    path('upload-payslip/', views.upload_payslips, name='upload-payslip'),

    path('get_payslip_url/<str:payslip_id>/', views.get_payslip_url, name='get_payslip_url'),
    path('send-payslip/<str:pk>/', views.send_payslip_email, name='send-payslip'),
]
