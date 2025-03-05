from .models import Notification

def notification_context_processor(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(reciever=request.user).order_by('-notified_at')
        notif_count = Notification.objects.filter(reciever=request.user, is_seen=False).count()
    else:
        notifications = [] 
        notif_count = 0 

    return {'notifications': notifications, 'notif_count': notif_count}