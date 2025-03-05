from django.contrib import admin
from .models import Training, ParticipantResponse, TrainingForm, TrainingApproval


admin.site.register(Training)
admin.site.register(ParticipantResponse)
admin.site.register(TrainingForm)
admin.site.register(TrainingApproval)
