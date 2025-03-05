from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='greeting')
def greeting(name):
    current_time = timezone.localtime()
    if current_time.hour < 12:
        return f"Good morning, {name}"
    elif 12 <= current_time.hour < 18:
        return f"Good afternoon, {name}"
    else:
        return f"Good evening, {name}"
