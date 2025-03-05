from django.db import models
from UserLogin.models import EmployeeLogin

class PRForm(models.Model):
    request_by = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='prform_requestor')
    request_type = models.CharField(max_length=50, null=True)
    ctrl_no = models.CharField(max_length=50, null=True, default='N/A')
    status = models.CharField(max_length=20, null=True)
    purpose = models.TextField()
    approved_by = models.CharField(max_length=100, null=True, default="-")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.request_by}-{self.request_type}'
