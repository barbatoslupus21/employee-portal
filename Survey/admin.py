from django.contrib import admin
from .models import SurveyForm, Quarter, UserResponse

admin.site.register(SurveyForm)
admin.site.register(Quarter)
admin.site.register(UserResponse)
