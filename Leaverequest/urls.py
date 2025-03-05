from django.urls import path
from . import views
urlpatterns = [
    
    path('leave-filing/', views.leave_view, name='leave'),
    path('submit-leave/', views.submit_leave, name='submit-leaverequest'),
    path('delete-leave/<str:pk>/', views.delete_leave, name='delete-leave'),
    path('leave-history/', views.leave_history, name='leave-history'),

    path('admin_leave/', views.leave_balances, name='leave-balances'),
    path('upload-balance/', views.import_balances, name='upload-balances'),
    path('admin-approval/', views.admin_approval, name='admin-approval'),
    path('admin-approval/<str:pk>/', views.admin_leave_approval, name='admin_leave_approval'),
    path('leavelists/', views.admin_leavelist, name='admin-leave'),
    path('export-leave/', views.export_leave_excel, name='export-leave'),
    path('pending-leave/', views.export_pending_leave, name='pending-leave'),

    path('api/leave-percentages/', views.department_percentages_leave),  
    path('leave/get-categories/', views.get_leave_categories),
    path('api/calculate-leave-days/', views.calculate_leave_days),
    path('api/leaverouting/<int:leave_request_id>/', views.LeaveRoutingListAPIView.as_view()),
    path('api/leave-percentage/', views.leave_request_percentage_view, name='leave_percentage')
]
