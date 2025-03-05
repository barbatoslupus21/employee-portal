from django.shortcuts import render, redirect, get_object_or_404
from .models import Announcements
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def announcement_view(request):
    if not request.user.is_hr:
        messages.error(request, "You don't have the authority to open this section.")
        return redirect(request.META.get('HTTP_REFERER'))

    announcements = Announcements.objects.all().order_by('-posted_at')
    return render(request, 'Announcements/admin-announce.html', {'announcements':announcements})

@login_required(login_url='login')
def create_announcement(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        poster = request.FILES.get('poster')

        AnnouncementsForm = Announcements(
            image=poster,
            title=title,
            description=description
        )

        AnnouncementsForm.save()
        messages.success(request, 'Announcement created successfully.')
        return redirect('announcements')
    return redirect('announcements')

@login_required(login_url='login')
def delete_announcement(request, pk):
    selectedAnnouncement = get_object_or_404(Announcements, id=pk)

    if request.method == "POST":
        selectedAnnouncement.delete()
        messages.success(request, 'Announcement deleted.')
        return redirect('announcements')
    return redirect('announcements')

