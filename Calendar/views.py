from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EventRepetition, EventType, Event
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer, format_events_as_holidays

@login_required(login_url='login')
def admin_calendar_view(request):
    if request.user.is_hr == False:
        messages.error(request, "You don't have the authority to open this section.")
        return redirect(request.META.get('HTTP_REFERER'))
    try:
        events = Event.objects.all().order_by('event_date')
        repetitions = EventRepetition.objects.all()
        types = EventType.objects.all()
    except Event.DoesNotExist:
        events = None
        repetitions = None
        types = None

    context = {
        'events': events,
        'repetitions':repetitions,
        'types':types
    }

    return render(request, 'Calendar/admin-calendar.html', context)

@login_required(login_url='login')
def submit_event(request):
    repetitions = EventRepetition.objects.all()
    types = EventType.objects.all()

    if request.method == "POST":
        event_date = request.POST.get('event_date')
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')

        repetition = request.POST.get('event_repeat')
        event_repetition = EventRepetition.objects.get(name=repetition)

        type_name = request.POST.get('event_type')
        event_type = EventType.objects.get(name=type_name)

        event_image = request.FILES.get('event_picture')

        EventForm = Event(
            event_date=event_date,
            event_name=event_name,
            event_description=event_description,
            event_repetition=event_repetition,
            event_type=event_type,
            event_image=event_image
        )

        EventForm.save()
        messages.success(request, 'Event submitted successfully.')
        return redirect('admin-calendar')
    else:
        return render(request, 'Calendar/admin-calendar.html', {'repetitions':repetitions, 'types':types})
    
@login_required(login_url='login')
def edit_event(request, pk):
    selectedEvent = get_object_or_404(Event, id=pk)
    repetitions = EventRepetition.objects.all()
    types = EventType.objects.all()

    if request.method == "POST":
        event_date = request.POST.get('event_date')
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')

        repetition = request.POST.get('event_repeat')
        event_repetition = EventRepetition.objects.get(name=repetition)

        type_name = request.POST.get('event_type')
        event_type = EventType.objects.get(name=type_name)

        event_image = request.FILES.get('event_image')

        selectedEvent.event_date=event_date
        selectedEvent.event_name=event_name
        selectedEvent.event_description=event_description
        selectedEvent.event_repetition=event_repetition
        selectedEvent.event_type=event_type
        if event_image:
            selectedEvent.event_image = event_image
        
        selectedEvent.save()
        messages.success(request, 'Event submitted successfully.')
        return redirect('admin-calendar')
    
    context = {
        'repetitions':repetitions,
        'types':types,
        'selectedEvent':selectedEvent
    }
    return render(request, 'Calendar/admin-calendar.html', context)

@login_required(login_url='login')
def event_delete(request, pk):
    deleteEvent = get_object_or_404(Event, id=pk)
    
    if request.method == 'POST':
        deleteEvent.delete()
        messages.success(request, 'Event deleted.')
        return redirect('admin-calendar')
    else:
        messages.warning(request, 'Invalid request method.')
    
    return redirect('admin-calendar')

@api_view(['GET'])
def event_list(request):
    events = Event.objects.all().order_by('event_date')
    holidays = format_events_as_holidays(events)
    return Response(holidays)

@login_required(login_url='login')
def calendar_view(request):
    return render(request, 'Calendar/calendar.html')