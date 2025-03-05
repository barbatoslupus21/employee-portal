from django.contrib import admin
from .models import EventRepetition, Event, EventType

admin.site.register(EventType)
admin.site.register(EventRepetition)
admin.site.register(Event)
