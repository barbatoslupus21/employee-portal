from django.urls import path
from . import views
urlpatterns = [
    
    path('general-settings/', views.general_settings, name='settings'),

    path('edit-office/<str:pk>/', views.edit_office, name='edit-office'),
    path('delete-office/<str:pk>/', views.delete_office, name='delete-office'),
    path('create-office/', views.create_office, name='create-office'),

    path('edit-location/<str:pk>/', views.edit_location, name='edit-location'),
    path('delete-location/<str:pk>/', views.delete_location, name='delete-location'),
    path('create-location/', views.create_location, name='create-location'),

    path('edit-department/<str:pk>/', views.edit_department, name='edit-department'),
    path('delete-department/<str:pk>/', views.delete_department, name='delete-department'),
    path('create-department/', views.create_department, name='create-department'),

    path('edit-line/<str:pk>/', views.edit_line, name='edit-line'),
    path('delete-line/<str:pk>/', views.delete_line, name='delete-line'),
    path('create-line/', views.create_line, name='create-line'),

    path('edit-status/<str:pk>/', views.edit_status, name='edit-status'),
    path('delete-status/<str:pk>/', views.delete_status, name='delete-status'),
    path('create-status/', views.create_status, name='create-status'),

    path('edit-position/<str:pk>/', views.edit_position, name='edit-position'),
    path('delete-position/<str:pk>/', views.delete_position, name='delete-position'),
    path('create-position/', views.create_position, name='create-position'),

    path('edit-gender/<str:pk>/', views.edit_gender, name='edit-gender'),
    path('delete-gender/<str:pk>/', views.delete_gender, name='delete-gender'),
    path('create-gender/', views.create_gender, name='create-gender'),

    path('edit-leavetype/<str:pk>/', views.edit_leavetype, name='edit-leavetype'),
    path('delete-leavetype/<str:pk>/', views.delete_leavetype, name='delete-leavetype'),
    path('create-leavetype/', views.create_leavetype, name='create-leavetype'),

    path('edit-category/<str:pk>/', views.edit_category, name='edit-category'),
    path('delete-category/<str:pk>/', views.delete_category, name='delete-category'),
    path('create-category/', views.create_category, name='create-category'),

    path('edit-certificate/<str:pk>/', views.edit_settings_certificate, name='edit-setting-certificate'),
    path('delete-certificate/<str:pk>/', views.delete_settings_certificate, name='delete-setting-certificate'),
    path('create-certificate/', views.create_settings_certificate, name='create-setting-certificate'),

    path('edit-speaker/<str:pk>/', views.edit_speaker, name='edit-speaker'),
    path('delete-speaker/<str:pk>/', views.delete_speaker, name='delete-speaker'),
    path('create-speaker/', views.create_speaker, name='create-speaker'),

    path('edit-signer/<str:pk>/', views.edit_signer, name='edit-signer'),
    path('delete-signer/<str:pk>/', views.delete_signer, name='delete-signer'),
    path('create-signer/', views.create_signer, name='create-signer'),

    path('edit-eventtype/<str:pk>/', views.edit_event_type, name='edit-eventtype'),
    path('delete-eventtype/<str:pk>/', views.delete_event_type, name='delete-eventtype'),
    path('create-eventtype/', views.create_event_type, name='create-eventtype'),

    path('edit-repetition/<str:pk>/', views.edit_repetition, name='edit-repetition'),
    path('delete-repetition/<str:pk>/', views.delete_repetition, name='delete-repetition'),
    path('create-repetition/', views.create_repetition, name='create-repetition'),

    path('edit-newscategory/<str:pk>/', views.edit_newscategory, name='edit-newscategory'),
    path('delete-newscategory/<str:pk>/', views.delete_newscategory, name='delete-newscategory'),
    path('create-newscategory/', views.create_newscategory, name='create-newscategory'),

    path('edit-destination/<str:pk>/', views.edit_destination, name='edit-destination'),
    path('delete-destination/<str:pk>/', views.delete_destination, name='delete-destination'),
    path('create-destination/', views.create_destination, name='create-destination'),

    path('edit-pickup/<str:pk>/', views.edit_pickup, name='edit-pickup'),
    path('delete-pickup/<str:pk>/', views.delete_pickup, name='delete-pickup'),
    path('create-pickup/', views.create_pickup, name='create-pickup'),

    path('edit-ticket-category/<str:pk>/', views.edit_ticket_category, name='edit-ticket-category'),
    path('delete-ticket-category/<str:pk>/', views.delete_ticket_category, name='delete-ticket-category'),
    path('create-ticket-category/', views.create_ticket_category, name='create-ticket-category'),

    path('edit-ticket-level/<str:pk>/', views.edit_ticket_level, name='edit-ticket-level'),
    path('delete-ticket-level/<str:pk>/', views.delete_ticket_level, name='delete-ticket-level'),
    path('create-ticket-level/', views.create_ticket_level, name='create-ticket-level'),
    
]
