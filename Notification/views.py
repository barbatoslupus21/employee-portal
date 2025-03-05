from django.urls import reverse
from django.utils.timesince import timesince
from .models import Notification
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def get_notifications_api(request):
    notifications = Notification.objects.filter(
        reciever=request.user
    ).select_related('notifier').order_by('-notified_at')
    
    notification_data = []
    for notif in notifications:
        notification_data.append({
            'id': notif.id,
            'notifier_name': notif.notifier.name,
            'notifier_avatar': notif.notifier.avatar.url,
            'message': notif.message,
            'is_seen': notif.is_seen,
            'remarks': notif.remarks,
            'page': reverse(notif.page),
            'notified_at': notif.notified_at.strftime("%B %d, %Y %I:%M %p"),
            'timesince': f"{timesince(notif.notified_at)} ago"
        })
    
    unread_count = notifications.filter(is_seen=False).count()
    
    return JsonResponse({
        'notifications': notification_data,
        'unread_count': unread_count
    })

@login_required(login_url='login')
def mark_notification_as_seen(request, notification_id):
    if request.method == 'POST':
        try:
            notification = Notification.objects.get(
                id=notification_id, 
                reciever=request.user
            )
            notification.is_seen = True
            notification.save()
            return JsonResponse({'status': 'success'})
        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return JsonResponse({'status': 'error'}, status=400)
