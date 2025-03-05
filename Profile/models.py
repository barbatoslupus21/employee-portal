from django.db import models
from UserLogin.models import EmployeeLogin
from Settings.models import CompanyOffice, Location, Lines, Department, Status, Position, Gender
from Overtime.models import PickUpPoint
    
class PersonalInformation(models.Model):
    name = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, blank=True, null=True, related_name='personal_info')
    middlename = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=20, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=11, null=True)
    mother = models.CharField(max_length=100, null=True)
    father = models.CharField(max_length=100, null=True)
    work_email = models.EmailField(unique=True, null=True, blank=True)

    present_street = models.CharField(max_length=200, null=True)
    present_baranggay = models.CharField(max_length=200, null=True)
    present_city = models.CharField(max_length=200, null=True)
    present_province = models.CharField(max_length=200, null=True)
    
    provincial_street = models.CharField(max_length=200, null=True)
    provincial_baranggay = models.CharField(max_length=200, null=True)
    provincial_city = models.CharField(max_length=200, null=True)
    provincial_province = models.CharField(max_length=200, null=True)

    contact_firstname = models.CharField(max_length=100, null=True)
    contact_middlename = models.CharField(max_length=100, null=True)
    contact_lastname = models.CharField(max_length=100, null=True)
    contact_relation = models.CharField(max_length=100, null=True)
    contact_no = models.CharField(max_length=11, null=True)
    contact_street = models.CharField(max_length=200, null=True)
    contact_baranggay = models.CharField(max_length=200, null=True)
    contact_city = models.CharField(max_length=200, null=True)
    contact_province = models.CharField(max_length=200, null=True)

    primary_school = models.CharField(max_length=200, null=True)
    secondary_school = models.CharField(max_length=200, null=True)
    vocational_school = models.CharField(max_length=200, null=True)
    tertiary_school = models.CharField(max_length=200, null=True)
    spouse = models.CharField(max_length=100, null=True)
    no_of_children = models.CharField(max_length=2, null=True)
    children = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name.name
    
class EmploymentInformation(models.Model):
    name = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, blank=True, related_name='employment_info')
    approver = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='user_approver', null=True, blank=True)
    shuttle = models.ForeignKey(PickUpPoint, on_delete=models.CASCADE, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    line = models.ForeignKey(Lines, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    Status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=100, null=True)
    date_hired = models.DateField()
    tin_number = models.CharField(max_length=100, null=True)
    sss_number = models.CharField(max_length=100, null=True)
    hdmf_number = models.CharField(max_length=100, null=True)
    philhealth = models.CharField(max_length=100, null=True)
    bank_account = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name.name
    