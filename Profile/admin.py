from django.contrib import admin
from .models import PersonalInformation, EmploymentInformation

admin.site.register(PersonalInformation)
admin.site.register(EmploymentInformation)