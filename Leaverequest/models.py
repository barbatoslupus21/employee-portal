from django.db import models
from UserLogin.models import EmployeeLogin

class LeaveType(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
    
class LeaveCategory(models.Model):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.leave_type}-{self.category_name}'

class LeaveBalances(models.Model):
    name = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, null=True)
    date_started = models.DateField()
    date_ended = models.DateField()
    balances = models.CharField(max_length=2, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.name}-{self.leave_type}'
    
class LeaveRequest(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    days = models.CharField(max_length=3, null=True)
    hrs = models.CharField(max_length=3, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    category = models.ForeignKey(LeaveCategory, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=10, default="On Process")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.name} - {self.leave_type.name}'
    
class LeaveRouting(models.Model):
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE, related_name='routings')
    approver = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Waiting for Approval')
    remarks = models.TextField(blank=True)
    request_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.approver.name} - {self.leave_request.employee.name}'


