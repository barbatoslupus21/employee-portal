from django.db import models
from UserLogin.models import EmployeeLogin

class PerformanceEvaluation(models.Model):
    quarter = models.CharField(max_length=100, null=True)
    period = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100, default="OPEN")
    created_by = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quarter
    
class Tasklist(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    tasklist = models.TextField()
    def __str__(self):
        return f'{self.employee.idnumber} - {self.employee.name}'
    
class EmployeeResponse(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    quarter = models.ForeignKey(PerformanceEvaluation, on_delete=models.CASCADE)
    is_evaluated = models.BooleanField(default=False)
    date_submitted = models.DateField(null=True)
    is_submitted = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.employee} - {self.quarter}'
    
class PerformanceRouting(models.Model):
    evaluation = models.ForeignKey(EmployeeResponse, on_delete=models.CASCADE)
    approver = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="Pending")
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.approver.name} - {self.evaluation}'
    
class Assessment(models.Model):
    response = models.ForeignKey(EmployeeResponse, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    tasklist = models.TextField()
    self_assessment = models.CharField(max_length=2, null=True, blank=True)
    supervisor_assessment = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.employee.name
    
class RecommendationsConcerns(models.Model):
    response = models.ForeignKey(EmployeeResponse, on_delete=models.CASCADE, null=True) 
    strength = models.TextField(blank=True)
    weakness = models.TextField(blank=True)
    training_required = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    emp_comment = models.TextField(blank=True)
    manager_comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.response.employee.name} - {self.response.quarter.quarter}'
    
class TrainingRequest(models.Model):
    response = models.ForeignKey(EmployeeResponse, on_delete=models.CASCADE, null=True) 
    training = models.TextField()
    objective = models.TextField()

    def __str__(self):
        return f'{self.response.employee} - {self.training}'