from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('Mainpage.urls')),
    path('Login/', include('UserLogin.urls')),
    path('Dashboard/', include('Dashboard.urls')),
    path('The-wire/', include('TheWire.urls')),
    path('Calendar/', include('Calendar.urls')),
    path('Timelogs/', include('Timelogs.urls')),
    path('Profile/', include('Profile.urls')),
    path('Prform/', include('Prform.urls')),
    path('Survey/', include('Survey.urls')),
    path('Feedback/', include('Feedback.urls')),
    path('Training-effectiveness/', include('Training.urls')),
    path('Settings/', include('Settings.urls')),
    path('Notification/', include('Notification.urls')),
    path('Certificate/', include('Certificate.urls')),
    path('Finance/', include('Accounting.urls')),
    path('Announcements/', include('Announcements.urls')),
    path('Leave/', include('Leaverequest.urls')),
    path('Evaluation/', include('Evaluation.urls')),
    path('Overtime/', include('Overtime.urls')),
    path('Ticket/', include('Ticketing.urls')),
    path('Pages/', include('Pages.urls')),
]

if settings.DEBUG:  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  