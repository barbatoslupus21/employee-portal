from django.db import models
from UserLogin.models import EmployeeLogin

class EmployeeTimelogs(models.Model):
    employee_id = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    log_date = models.DateField()
    time_in = models.CharField(max_length=10, null=True, blank=True)
    time_out = models.CharField(max_length=10, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_id.name