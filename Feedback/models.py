from django.db import models
from UserLogin.models import EmployeeLogin

class UserFeedback(models.Model):
    employee = models.CharField(max_length=100, null=True)
    feedback = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)\
    
    def __str__(self):
        return f'{self.employee} - {self.submitted_at}'


