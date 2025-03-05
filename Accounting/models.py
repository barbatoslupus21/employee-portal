from django.db import models
from UserLogin.models import EmployeeLogin
import os
from django.core.exceptions import ValidationError
from datetime import datetime, date

class FinanceType(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(FinanceType, on_delete=models.CASCADE)
    date_started = models.DateField()
    loan_amount = models.CharField(max_length=100, null=True)
    payment = models.CharField(max_length=50, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.name} - {self.loan_type.name}'
    
class Savings(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    savings_type = models.ForeignKey(FinanceType, on_delete=models.CASCADE)
    date_started = models.DateField()
    desired_savings = models.CharField(max_length=100, null=True)
    savings = models.CharField(max_length=50, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.name} - {self.savings_type.name}'
    
class Medicine(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    type = models.ForeignKey(FinanceType, on_delete=models.CASCADE)
    started_at = models.DateField()
    ended_at = models.DateField()
    amount = models.CharField(max_length=20, null=True)
    claimed_amount= models.CharField(max_length=20, null=True)
    balance = models.CharField(max_length=20, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee} - {self.type.name}'
    
class PerfectAttendance(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    type = models.ForeignKey(FinanceType, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True)
    started_at = models.DateField()
    ended_at = models.DateField()
    amount = models.CharField(max_length=20, null=True)
    is_credited = models.BooleanField(default=False)
    date_credited = models.DateField(null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee} - {self.title}'
    
def validate_file_size(value):
    filesize = value.size
    if filesize > 400 * 1024:
        raise ValidationError("The maximum file size that can be uploaded is 400KB")

def payslip_upload_path(instance, filename):
    employee_id = os.path.splitext(filename)[0]
    payroll_start = instance.payroll_start.strftime('%Y%m%d')
    payroll_end = instance.payroll_end.strftime('%Y%m%d')
    cutoff_date = f"{payroll_start}-{payroll_end}"
    new_filename = f"{employee_id}-{cutoff_date}.pdf"
    
    return os.path.join('payslips', new_filename)

class EmployeePayslip(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    payroll_start = models.DateField(null=True)
    payroll_end = models.DateField(null=True)
    payslip = models.FileField(
        upload_to=payslip_upload_path,
        validators=[validate_file_size]
    )
    status = models.CharField(max_length=10, default="Pending")
    received_date = models.DateTimeField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['employee', 'payroll_start', 'payroll_end']

    def __str__(self):
        return f'{self.employee.idnumber} - {self.payroll_start} to {self.payroll_end}'
    
