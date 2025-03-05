from django.urls import path
from . import views

urlpatterns = [
    
    path('profile/', views.profile_view, name='user-profile'),
    path('update-profile/', views.save_profile, name='update-profile'),
    path('edit-profile/', views.update_profile, name='edit-profile'),
    path('account-settings/', views.account_setting, name='account-settings'),
    path('deactivate-account/<str:pk>/', views.deactivate_account, name="deactivate"),
    path('change-password/', views.change_password, name='change-password'),

    path('employee-accounts/', views.employee_accounts, name='accounts'),
    path('approval/<int:pk>/<str:action>/', views.approval, name='approval'),
    path('reset-password/<str:pk>/', views.reset_password, name="reset-password"),
    path('view-account/<str:pk>/', views.account_view, name="view-account"),
    path('update-account/<str:pk>/', views.edit_account, name='update-account'),
    path('import-employment/', views.employment_info_import, name='import-employment'),
    path('import-personal/', views.personal_info_import, name='import-personal'),
    path('lock-account/<str:pk>/', views.lock_account, name='lock-account'),
    path('unlock-account/<str:pk>/', views.unlock_account, name='unlock-account'),
    path('import-accounts/', views.account_import, name='import-account'),
    
    path('export-masterlist', views.export_excel, name='export-info'),
    path('id-replacement/', views.id_request, name='id-request'),
    path('id-request/<int:pk>/approve/', views.id_request_status, {'action': 'approve'}, name='approve-id'),
    path('id-request/<int:pk>/disapprove/', views.id_request_status, {'action': 'disapprove'}, name='disapprove-id'),
    path('export-id-request/', views.export_id_request, name='export-id-request'),
    path('export-all/', views.export_all_employees, name='export-all-employees'),

    path('api/department-percentages/', views.department_percentages),
    path('api/profile-completion-percentage/', views.profile_completion_percentage, name='profile-completion-percentage'),
]
