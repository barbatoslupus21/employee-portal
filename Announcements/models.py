from django.db import models
from UserLogin.models import EmployeeLogin

class Announcements(models.Model):
    image = models.ImageField(upload_to='announcements/', null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
