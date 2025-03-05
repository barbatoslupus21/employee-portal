from rest_framework import serializers
from .models import Event
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    event_color = serializers.CharField(source='event_type.color', read_only=True)

    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_image', 'event_color']

def format_events_as_holidays(events):
    holidays = {}
    
    for event in events:
        event_data = {
            "event_name": event.event_name,
            "event_description": event.event_description,
            "event_image": event.event_image.url if event.event_image else None,
            "event_color": event.event_type.color
        }
        
        event_date_str = event.event_date.strftime('%Y-%m-%d')
        
        if event_date_str not in holidays:
            holidays[event_date_str] = []
        
        holidays[event_date_str].append(event_data)
    
    return holidays

