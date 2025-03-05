from django.contrib import admin
from .models import Destination, PickUpPoint, SupervisorGroup, OvertimeGroup, GroupEmployees, ShiftingSchedule

admin.site.register(Destination)
admin.site.register(PickUpPoint)
admin.site.register(SupervisorGroup)
admin.site.register(OvertimeGroup)
admin.site.register(GroupEmployees)
admin.site.register(ShiftingSchedule)
