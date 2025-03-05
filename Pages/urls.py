from django.urls import path
from . import views as pages_views

handler404 = pages_views.custom_404_view
handler500 = pages_views.custom_500_view

# Define your URL patterns
urlpatterns = [
    # Example URL pattern
    path('404/', pages_views.custom_404_view, name='404'),
    path('500/', pages_views.custom_500_view, name='500'),
]
