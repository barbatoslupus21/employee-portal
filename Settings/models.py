from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name
    
class CompanyOffice(models.Model):
    site = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.site
    
class Location(models.Model):
    location = models.CharField(max_length=100, null=True)
    site = models.ForeignKey(CompanyOffice, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.location}-{self.site}'
    
class Department(models.Model):
    abreviation = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.abreviation
    
class Lines(models.Model):
    line = models.CharField(max_length=100, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.line}-{self.location}'

class Status(models.Model):
    name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name
    
class Position(models.Model):
    name = models.CharField(max_length=100, null=True)
    is_approver = models.BooleanField(default=False)
    approver_level = models.IntegerField(default=1)
    def __str__(self):
        return self.name