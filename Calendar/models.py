from django.db import models

class EventRepetition(models.Model):
    name = models.CharField(max_length=100, null=True)
    duration = models.IntegerField()

    def __str__(self):
        return self.name
    
class EventType(models.Model):
    name = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return self.name

class Event(models.Model):
    event_date = models.DateTimeField()
    event_name = models.CharField(max_length=100, null=True)
    event_description = models.TextField(null=True)
    event_repetition = models.ForeignKey(EventRepetition, on_delete=models.CASCADE, null=True)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, null=True)
    event_image = models.ImageField(upload_to='calendar/', blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.event_name}-{self.event_date}'