from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Gender, CompanyOffice, Location, Department, Lines, Status, Position
from Leaverequest.models import LeaveType, LeaveCategory
from Certificate.models import CertSpeaker, Certificate, SigningAuthority
from Calendar.models import EventType, EventRepetition
from TheWire.models import NewCategory
from Overtime.models import Destination, PickUpPoint
from Ticketing.models import TicketCategory, TicketLevel

def is_admin(user):
    return user.is_admin

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='Dashboard:Dashboard')
def general_settings(request):

    if request.user.is_superuser == False:
        messages.error(request, "You don't have the authority to open this section.")
        return redirect(request.META.get('HTTP_REFERER'))
    
    genders = Gender.objects.all()
    offices = CompanyOffice.objects.all()
    locations = Location.objects.all()
    departments = Department.objects.all()
    lines = Lines.objects.all()
    statuses = Status.objects.all()
    positions = Position.objects.all()
    leavetypes = LeaveType.objects.all()
    categories = LeaveCategory.objects.all().order_by('leave_type')
    certificates = Certificate.objects.all().order_by('certificate_type')
    speakers = CertSpeaker.objects.all().order_by('name')
    signers = SigningAuthority.objects.all().order_by('certificate__title')
    event_types = EventType.objects.all()
    event_repetitions = EventRepetition.objects.all()
    news_categories = NewCategory.objects.all()
    destinations = Destination.objects.all()
    pick_ups = PickUpPoint.objects.all()
    ticket_categories = TicketCategory.objects.all()
    ticket_levels = TicketLevel.objects.all()
    context={
        'genders':genders,
        'offices':offices,
        'locations':locations,
        'departments':departments,
        'lines':lines,
        'statuses':statuses,
        'positions':positions,
        'leavetypes':leavetypes,
        'categories':categories,
        'certificates':certificates,
        'speakers':speakers,
        'signers':signers,
        'event_types':event_types,
        'event_repetitions':event_repetitions,
        'news_categories':news_categories,
        'destinations':destinations,
        'pick_ups':pick_ups,
        'ticket_categories':ticket_categories,
        'ticket_levels':ticket_levels
    }
    return render(request, 'Settings/settings.html', context)

@login_required(login_url='login')
def edit_office(request, pk):
    selected = get_object_or_404(CompanyOffice, id=pk)

    if request.method == 'POST':
        site = request.POST.get('officesite')
        selected.site = site
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_office(request, pk):
    selected = get_object_or_404(CompanyOffice, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Office deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_office(request):
    if request.method == 'POST':
        site = request.POST.get('officesite')
        CompanyOffice.objects.create(
            site=site
        )
        messages.success(request, 'New offices created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#location
@login_required(login_url='login')
def edit_location(request, pk):
    selected = get_object_or_404(Location, id=pk)

    if request.method == 'POST':
        location = request.POST.get('location')
        site = request.POST.get('office')
        selectedSite = CompanyOffice.objects.get(id=site)

        selected.location = location
        selected.site = selectedSite

        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_location(request, pk):
    selected = get_object_or_404(Location, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Location deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_location(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        site = request.POST.get('office')
        selectedSite = CompanyOffice.objects.get(id=site)

        Location.objects.create(
            location=location,
            site=selectedSite
        )
        messages.success(request, 'New location created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#Department
@login_required(login_url='login')
def edit_department(request, pk):
    selected = get_object_or_404(Department, id=pk)

    if request.method == 'POST':
        abreviation = request.POST.get('abreviation')
        description = request.POST.get('description')

        selected.abreviation = abreviation
        selected.description = description

        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_department(request, pk):
    selected = get_object_or_404(Department, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Department deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_department(request):
    if request.method == 'POST':
        abreviation = request.POST.get('abreviation')
        description = request.POST.get('description')

        Department.objects.create(
            abreviation=abreviation,
            description=description
        )
        messages.success(request, 'New department created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#line
@login_required(login_url='login')
def edit_line(request, pk):
    selected = get_object_or_404(Lines, id=pk)

    if request.method == 'POST':
        line = request.POST.get('line')
        location = request.POST.get('location')
        selectedLocation = Location.objects.get(id=location)

        selected.line = line
        selected.location = selectedLocation

        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_line(request, pk):
    selected = get_object_or_404(Lines, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Line deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_line(request):
    if request.method == 'POST':
        line = request.POST.get('line')
        location = request.POST.get('location')
        selectedLocation = Location.objects.get(id=location)

        Lines.objects.create(
            line=line,
            location=selectedLocation
        )
        messages.success(request, 'New line created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#status
@login_required(login_url='login')
def edit_status(request, pk):
    selected = get_object_or_404(Status, id=pk)

    if request.method == 'POST':
        status = request.POST.get('status')

        selected.name = status
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_status(request, pk):
    selected = get_object_or_404(Status, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Status deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_status(request):
    if request.method == 'POST':
        status = request.POST.get('status')

        Status.objects.create(
            name=status
        )
        messages.success(request, 'New status created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#position
@login_required(login_url='login')
def edit_position(request, pk):
    selected = get_object_or_404(Position, id=pk)

    if request.method == 'POST':
        position = request.POST.get('position')
        level = request.POST.get('approver_level')

        selected.name = position
        selected.approver_level = level
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_position(request, pk):
    selected = get_object_or_404(Position, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Position deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_position(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        level = request.POST.get('approver_level')

        Position.objects.create(
            name=position,
            approver_level=level
        )
        messages.success(request, 'New position created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#gender
@login_required(login_url='login')
def edit_gender(request, pk):
    selected = get_object_or_404(Gender, id=pk)

    if request.method == 'POST':
        gender = request.POST.get('gender')
        selected.name = gender
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_gender(request, pk):
    selected = get_object_or_404(Gender, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Gender deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_gender(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')

        Gender.objects.create(
            name=gender
        )
        messages.success(request, 'New gender created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#leave types
@login_required(login_url='login')
def edit_leavetype(request, pk):
    selected = get_object_or_404(LeaveType, id=pk)

    if request.method == 'POST':
        leavetype = request.POST.get('leavetype')
        selected.name = leavetype
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_leavetype(request, pk):
    selected = get_object_or_404(LeaveType, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Leave type deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_leavetype(request):
    if request.method == 'POST':
        leavetype = request.POST.get('leavetype')

        LeaveType.objects.create(
            name=leavetype
        )
        messages.success(request, 'New leave type created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#leave category
@login_required(login_url='login')
def edit_category(request, pk):
    selected = get_object_or_404(LeaveCategory, id=pk)

    if request.method == 'POST':
        category = request.POST.get('category')
        leavetype = request.POST.get('leave_type')
        selectedLeave = LeaveType.objects.get(id=leavetype)

        selected.leave_type = selectedLeave
        selected.category_name = category
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_category(request, pk):
    selected = get_object_or_404(LeaveCategory, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Leave category deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        leavetype = request.POST.get('leave_type')
        selectedLeave = LeaveType.objects.get(id=leavetype)

        LeaveCategory.objects.create(
            leave_type = selectedLeave,
            category_name = category
        )
        messages.success(request, 'New leave category created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#certificates
@login_required(login_url='login')
def edit_settings_certificate(request, pk):
    selected = get_object_or_404(Certificate, id=pk)

    if request.method == 'POST':
        certificate_type = request.POST.get('certificate_type')
        title = request.POST.get('title')
        template = request.FILES.get('template')

        selected.certificate_type=certificate_type
        selected.title = title
        if template:
            selected.template = template
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_settings_certificate(request, pk):
    selected = get_object_or_404(Certificate, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Certificate deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_settings_certificate(request):
    if request.method == 'POST':
        certificate_type = request.POST.get('certificate_type')
        title = request.POST.get('title')
        template = request.FILES.get('template')

        Certificate.objects.create(
            certificate_type=certificate_type,
            title = title,
            template = template
        )
        messages.success(request, 'New certificate created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#speaker
@login_required(login_url='login')
def edit_speaker(request, pk):
    selected = get_object_or_404(CertSpeaker, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        signature = request.FILES.get('signature')

        selected.name=name
        selected.position = position
        if signature:
            selected.signature = signature
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_speaker(request, pk):
    selected = get_object_or_404(CertSpeaker, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Speaker deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_speaker(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        signature = request.FILES.get('signature')

        CertSpeaker.objects.create(
            name=name,
            position = position,
            signature = signature
        )
        messages.success(request, 'New speaker created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#signer
@login_required(login_url='login')
def edit_signer(request, pk):
    selected = get_object_or_404(SigningAuthority, id=pk)

    if request.method == 'POST':
        certificate = request.POST.get('certificate')
        selectedCertificate = Certificate.objects.get(id=certificate)
        signer = request.POST.get('signer')
        selectedSigner = CertSpeaker.objects.get(id=signer)

        selected.certificate=selectedCertificate
        selected.approver = selectedSigner
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_signer(request, pk):
    selected = get_object_or_404(SigningAuthority, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Signer deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_signer(request):
    if request.method == 'POST':
        certificate = request.POST.get('certificate')
        selectedCertificate = Certificate.objects.get(id=certificate)
        signer = request.POST.get('signer')
        selectedSigner = CertSpeaker.objects.get(id=signer)

        SigningAuthority.objects.create(
            certificate=selectedCertificate,
            approver = selectedSigner
        )
        messages.success(request, 'New signer created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#event types
@login_required(login_url='login')
def edit_event_type(request, pk):
    selected = get_object_or_404(EventType, id=pk)

    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        event_color = request.POST.get('event_color')
        selected.name = event_type
        selected.color = event_color
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_event_type(request, pk):
    selected = get_object_or_404(EventType, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Event type deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_event_type(request):
    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        event_color = request.POST.get('event_color')

        EventType.objects.create(
            name=event_type,
            color=event_color
        )
        messages.success(request, 'New event type created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#event repetition
@login_required(login_url='login')
def edit_repetition(request, pk):
    selected = get_object_or_404(EventRepetition, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        selected.name = name
        selected.duration = duration
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_repetition(request, pk):
    selected = get_object_or_404(EventRepetition, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Event repetition deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_repetition(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        EventRepetition.objects.create(
            name=name,
            duration=duration
        )
        messages.success(request, 'New event repetition created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#news category
@login_required(login_url='login')
def edit_newscategory(request, pk):
    selected = get_object_or_404(NewCategory, id=pk)

    if request.method == 'POST':
        category = request.POST.get('category')
        selected.category = category
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_newscategory(request, pk):
    selected = get_object_or_404(NewCategory, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'News category deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_newscategory(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        NewCategory.objects.create(
            category=category
        )
        messages.success(request, 'New category created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#destinations
@login_required(login_url='login')
def edit_destination(request, pk):
    selected = get_object_or_404(Destination, id=pk)

    if request.method == 'POST':
        location_name = request.POST.get('destination')
        selected.location_name = location_name
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_destination(request, pk):
    selected = get_object_or_404(Destination, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Destination deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_destination(request):
    if request.method == 'POST':
        location_name = request.POST.get('destination')
        Destination.objects.create(
            location_name=location_name
        )
        messages.success(request, 'New destination created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#pick up points
@login_required(login_url='login')
def edit_pickup(request, pk):
    selected = get_object_or_404(PickUpPoint, id=pk)

    if request.method == 'POST':
        pick_up = request.POST.get('pickup')
        location_name = request.POST.get('destination')
        selectedDestination = Destination.objects.get(id=location_name)

        selected.location_name = selectedDestination
        selected.pick_up = pick_up
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_pickup(request, pk):
    selected = get_object_or_404(PickUpPoint, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Pick-up point deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_pickup(request):
    if request.method == 'POST':
        pick_up = request.POST.get('pickup')
        location_name = request.POST.get('destination')
        selectedDestination = Destination.objects.get(id=location_name)

        PickUpPoint.objects.create(
            location_name=selectedDestination,
            pick_up=pick_up
        )
        messages.success(request, 'New pick-up point created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#ticket category
@login_required(login_url='login')
def edit_ticket_category(request, pk):
    selected = get_object_or_404(TicketCategory, id=pk)

    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')

        selected.category = category
        selected.description = description
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_ticket_category(request, pk):
    selected = get_object_or_404(TicketCategory, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Category deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_ticket_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')

        TicketCategory.objects.create(
            category=category,
            description=description
        )
        messages.success(request, 'New category created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

#ticket level
@login_required(login_url='login')
def edit_ticket_level(request, pk):
    selected = get_object_or_404(TicketLevel, id=pk)

    if request.method == 'POST':
        level = request.POST.get('level')

        selected.level = level
        selected.save()
        messages.success(request, 'Saved Changes.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def delete_ticket_level(request, pk):
    selected = get_object_or_404(TicketLevel, id=pk)
    if request.method == 'POST':
        selected.delete()
        messages.success(request, 'Level deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')

@login_required(login_url='login')
def create_ticket_level(request):
    if request.method == 'POST':
        level = request.POST.get('level')

        TicketLevel.objects.create(
            level=level
        )
        messages.success(request, 'New level created.')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('settings')