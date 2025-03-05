from django.urls import path
from . import views

urlpatterns = [

  path('survey/', views.survey_view, name='survey'),  
  path('take-survey/<str:pk>/', views.take_survey, name="take-survey"),
  path('response/<str:pk>/', views.survey_response, name='survey-response'),

  path('admin-survey/', views.admin_survey, name='admin-survey'),
  path('post-survey/', views.submit_quarter, name='post-survey'),
  path('edit-survey/<str:pk>/', views.edit_survey, name='edit-survey'),
  path('delete-survey/<str:pk>/', views.delete_survey, name='delete-survey'),
  path('view-survey/<str:pk>/', views.admin_survey_view, name='admin-view-survey'),
  path('close-survey/<str:pk>/', views.close_survey, name="close-survey"),
  path('export-survey/<int:pk>/', views.export_survey_excel, name='export-survey'),

  path('api/job-satisfaction/<str:pk>/', views.job_satisfaction),
  path('api/policy-salary/<str:pk>/', views.policy_salary),
  path('api/facilities/<str:pk>/', views.facilities),
  path('api/relation-program/<str:pk>/', views.relation_program),
  path('api/survey-rating-percentages/', views.SurveyRatingPercentagesView.as_view()),
]
