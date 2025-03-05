from django.db import models
from UserLogin.models import EmployeeLogin

class DeviceInformation(models.Model):
    Assigned_to = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='register_user')
    Device = models.CharField(max_length=50, null=True)
    Device_Name = models.CharField(max_length=50, null=True)
    Device_Code = models.CharField(max_length=50, null=True, unique=True)
    Device_location = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.Device_Code
    
class TicketCategory(models.Model):
    category = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category
    
class TicketLevel(models.Model):
    level = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.level
    
class MISTickets(models.Model):
    submitted_by = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, null=True)
    device = models.ForeignKey(DeviceInformation, on_delete=models.CASCADE, null=True, related_name='ticket_device')
    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE, null=True, blank=True) 
    level = models.ForeignKey(TicketLevel, on_delete=models.CASCADE, null=True, blank=True) 
    problem_summary = models.CharField(max_length=100, null=True)
    problem_details = models.TextField(null=True)
    status = models.CharField(max_length=100, default='On Process')
    technician = models.CharField(max_length=100, null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    action_taken = models.TextField(null=True, blank=True)
    possible_reason = models.TextField(null=True, blank=True)
    recommendation = models.TextField(null=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.submitted_by.name

