from django.contrib import admin
from .models import PerformanceEvaluation, PerformanceRouting, Tasklist, Assessment, EmployeeResponse, RecommendationsConcerns, TrainingRequest

admin.site.register(PerformanceRouting)
admin.site.register(PerformanceEvaluation)
admin.site.register(Tasklist)
admin.site.register(Assessment)
admin.site.register(EmployeeResponse)
admin.site.register(RecommendationsConcerns)
admin.site.register(TrainingRequest)