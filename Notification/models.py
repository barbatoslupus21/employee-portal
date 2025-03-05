from django.db import models
from UserLogin.models import EmployeeLogin

class Notification(models.Model):
    level = models.CharField(max_length=10, null=True)
    module = models.CharField(max_length=50, null=True)
    notifier = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='notif_notifier')
    page = models.CharField(max_length=200, null=True)
    reciever = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='notif_reciever')
    message = models.CharField(max_length=200, null=True)
    is_seen = models.BooleanField(default=False)
    remarks = models.TextField()
    notified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reciever.name}-{self.module}'
