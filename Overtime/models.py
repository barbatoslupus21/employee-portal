from django.db import models
from UserLogin.models import EmployeeLogin
from Settings.models import Lines, Department

class Destination(models.Model):
    location_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.location_name
    
class PickUpPoint(models.Model):
    location_name = models.ForeignKey(Destination, on_delete=models.CASCADE)
    pick_up = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f'{self.location_name} - {self.pick_up}'

class SupervisorGroup(models.Model):
    supervisor_leader = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='supervisor_group')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class OvertimeGroup(models.Model):
    supervisor_group = models.ForeignKey(SupervisorGroup, on_delete=models.CASCADE, related_name='sup_group')
    line_leader = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='line_leaders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('supervisor_group', 'line_leader')

class GroupEmployees(models.Model):
    group = models.ForeignKey(OvertimeGroup, on_delete=models.CASCADE, related_name='members')
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='group_memberships')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('group', 'employee')

class ShiftingSchedule(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    shift = models.CharField(max_length=2, null=True)
    supervisor = models.ForeignKey(SupervisorGroup, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.employee.name} - {self.shift} - {self.supervisor.supervisor_leader.name}'