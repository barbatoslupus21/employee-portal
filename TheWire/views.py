from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TheWireNews, NewCategory
from UserLogin.models import EmployeeLogin
from django.contrib import messages
from rest_framework import generics
from .serializers import TheWireNewsSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from Notification.models import Notification

@receiver(post_save, sender=TheWireNews)
def notification_for_users(sender, instance, created, **kwargs):
    if created:
        employees = EmployeeLogin.objects.all().exclude(is_admin=True, is_active=False)
        for employee in employees:
            Notification.objects.create(
                    level="Low",
                    module='TheWire',
                    notifier=instance.author,
                    page="the-wire",
                    reciever=employee,
                    message= f'has posted new company {instance.category.category} news.'
                )

@login_required(login_url='login')
def the_wire_view(request):
    try:  
        latest_news = TheWireNews.objects.latest('published_at')  
        headlines = TheWireNews.objects.exclude(id=latest_news.id).order_by('-published_at')[:10]  
    except TheWireNews.DoesNotExist:  
        latest_news = None 
        headlines = None
    categories = NewCategory.objects.all()

    context = {
        'headlines':headlines,
        'latest_news':latest_news,
        'categories':categories,
    }

    return render(request, 'TheWire/admin-the-wire.html', context)

@login_required(login_url='login')
def submit_news(request):
    categories = NewCategory.objects.all() 
    if request.method == 'POST':
        news_title = request.POST.get('headline')
        category = request.POST.get('category')
        news_category = NewCategory.objects.get(category=category)
        news_content = request.POST.get('article')
        news_image = request.FILES.get('articleImage')
        
        news_instance = TheWireNews(
            author=request.user,
            category=news_category,
            image=news_image,
            news_title=news_title,
            news_content=news_content
        )
        news_instance.save()
        messages.success(request, 'News submitted successfully.')
        return redirect('the-wire')
    else:
        return render(request, 'TheWire/admin-the-wire.html', {'categories': categories})
    
@login_required(login_url='login')
def view_news(request, pk):
    try:  
        selectedNews = TheWireNews.objects.get(id=pk)  
        otherNews = TheWireNews.objects.filter(category=selectedNews.category).exclude(id=selectedNews.id).order_by('-published_at')[:5]
    except TheWireNews.DoesNotExist:  
        latest_news = None 
        otherNews = None

    context = {
        'otherNews':otherNews,
        'selectedNews':selectedNews,
    }

    return render(request, 'TheWire/view-news.html', context)

@login_required(login_url='login')
def all_news(request):
    try:  
        allNews = TheWireNews.objects.all() 
    except TheWireNews.DoesNotExist:  
        allNews = None 

    context = {
        'allNews':allNews,
    }

    return render(request, 'TheWire/browse-news.html', context)

@login_required(login_url='login')
def news_delete(request, pk):
    deletedNews = get_object_or_404(TheWireNews, id=pk)
    
    if request.method == 'POST':
        deletedNews.delete()
        messages.success(request, 'News Deleted.')
        return redirect('browse-news')
    else:
        messages.error(request, 'Invalid request method.')
    
    return redirect('browse-news')


class TheWireNewsListView(generics.ListAPIView):
    queryset = TheWireNews.objects.all().order_by('-published_at')
    serializer_class = TheWireNewsSerializer