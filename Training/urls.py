from django.urls import path
from . import views

urlpatterns = [
    
    path('Admin-training/', views.admin_training, name='admin-training'),
    path('create-training/', views.create_training, name='create-training'),
    path('delete-training/<str:pk>/', views.delete_training, name='delete-training'),
    path('view-training/<str:pk>/', views.admin_view_training, name="view-training"),
    path('close-training/<str:pk>/', views.close_training, name="close-training"),
    path('delete-partiicipant/<str:pk>/', views.delete_participant, name="delete-participant"),
    path('view-participant/<str:pk>/', views.admin_response_view, name='admin-view-response'),
    path('export-training/<int:pk>/', views.export_training_excel, name='export-training'),

    path('training/', views.training, name="training"),
    path('training-evaluation/<str:pk>/', views.training_view, name='take-training'),
    path('submit-evaluation/<str:pk>/', views.participant_response, name='submit-training'),
    path('view-response/<str:pk>/', views.survey_response_view, name='view-response'),

    path('api/training-content/<str:pk>/', views.training_content),
    path('api/training-structure/<str:pk>/', views.training_structure),
    path('api/training-speaker/<str:pk>/', views.training_speaker),
    path('api/training-resources/<str:pk>/', views.training_resources),
    path('api/training-counts/', views.training_counts),

    path('evaluate-training/', views.supervisor_view, name="supervisor-view"),
    path('evaluate-participant/<str:pk>/', views.evaluate_participant, name='evaluate'),
    path('evaluate/<str:pk>/', views.submit_evaluation, name="submit-evaluation"),

    path('manager-approval/', views.manager_view, name='manager-training-view'),
    path('view-training-approval/<str:pk>/', views.manager_approval, name="manager-approval"),
    path('manager-training-approval/<str:pk>/', views.manager_training_approval, name='manager-training-approval'),
    
]
