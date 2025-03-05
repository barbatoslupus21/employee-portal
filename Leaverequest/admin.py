from django.contrib import admin
from .models import LeaveType, LeaveCategory, LeaveBalances, LeaveRequest, LeaveRouting

admin.site.register(LeaveType)
admin.site.register(LeaveCategory)
admin.site.register(LeaveBalances)
admin.site.register(LeaveRequest)
admin.site.register(LeaveRouting)
