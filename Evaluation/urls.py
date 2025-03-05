from django.urls import path
from . import views

urlpatterns = [
    
    path('admin-performance-evaluation/', views.admin_evaluation, name='admin-performance'),
    path('create-evaluation/', views.create_evaluation, name='create-performance'),
    path('edit-evaluation/<str:pk>/', views.edit_evaluation, name='edit-performance'),
    path('delete-evaluation/<str:pk>/', views.delete_evaluation, name='delete-performance'),
    path('view-responses/<str:pk>/', views.evaluation_view_response, name="view-quarter-response"),
    path('close-performance-evaluation/<str:pk>/', views.close_survey, name="close-performance"),
    path('upload-tasklists/', views.import_tasklists, name="upload-tasklist"),
    path('employee-response/<str:pk>/', views.view_employee_response, name="view-employee-response"),

    path('performance-evaluation/', views.evaluation_view, name='performance-evaluation'),
    path('evaluation-form/<str:pk>/', views.evaluation_form, name="performance-evaluation-form"),
    path('submit-form/<str:pk>/', views.submit_evaluation_form, name="submit-evalform"),

    path('employee-performance-evaluation/', views.supervisor_evaluation_view, name="supervisor-evaluation"),
    path('view-quarter/<str:pk>/', views.supervisor_view_quarter, name="supervisor-view-quarter"),
    path('supervisor-assessment/<str:pk>/', views.supervisor_assessment, name='supervisor-assessment'),
    path('submit-assessment/<str:pk>/', views.supervisor_assessment_update, name="submit-assessment"),

    path('employee-evaluation/', views.manager_evaluation_view, name="manager-view"),
    path('view-quarter-evaluation/<str:pk>/', views.manager_view_quarter, name="manager-view-quarter"),
    path('employee-performance/<str:pk>/', views.manager_evaluation, name="manager-evaluation"),
    path('performance-evaluation-approval/<str:pk>/', views.manager_evaluation_approval, name="manager-evaluation-approval"),
    path('export-performance-evaluation/<str:pk>/', views.export_data_to_excel, name="export-performance-evaluation"),
]
