from django.db import models
from django.contrib.auth.models import AbstractUser

class EmployeeLogin(AbstractUser):
    avatar = models.ImageField(upload_to='profile/', null=True, default='avatar.svg') 
    idnumber = models.CharField(max_length=10, null=True)
    username = models.CharField(max_length=20, unique=True, null=True)
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, blank=True)
    is_approver = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_locked = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_the_wire = models.BooleanField(default=False)
    is_clinic = models.BooleanField(default=False)
    is_iad = models.BooleanField(default=False)
    is_accounting = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_hrmanager = models.BooleanField(default=False)
    is_approved = models.CharField(max_length=20, default='For Approval')
    is_mis = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_ot_coordinator = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

