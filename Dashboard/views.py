from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from UserLogin.models import EmployeeLogin
from Announcements.models import Announcements
from Profile.models import EmploymentInformation
from Profile.models import PersonalInformation
from django.utils import timezone
import requests

@login_required(login_url='login')
def user_dashboard(request):
    # Fetch announcements
    announcements = Announcements.objects.all().order_by('-posted_at')
    
    is_birthday = PersonalInformation.objects.filter(name=request.user).first()
    current_date = timezone.now().date()

    age = None
    if is_birthday and is_birthday.birth_date:
        age = current_date.year - is_birthday.birth_date.year
        if (current_date.month, current_date.day) < (is_birthday.birth_date.month, is_birthday.birth_date.day):
            age -= 1

    api_key = '1e7a89c02670496fb31233531241410'
    city = 'Biñan, Laguna'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    
    is_rainy = False
    is_sunny = False
    greeting = "Good day"
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        weather_condition = weather_data['current']['condition']['text'].lower()
        
        is_rainy = 'rain' in weather_condition or 'drizzle' in weather_condition
        is_sunny = 'sun' in weather_condition or 'clear' in weather_condition

        current_time = timezone.localtime()
        if current_time.hour < 12:
            greeting = "Good morning" if is_sunny else "Good Morning"
        elif 12 <= current_time.hour < 18:
            greeting = "Good afternoon" if is_sunny else "Good Afternoon"
        else:
            greeting = "Good evening" if is_sunny else "Good Evening"
        
    except requests.exceptions.RequestException:
        pass

    context = {
        'announcements': announcements,
        'is_birthday': is_birthday,
        'age': age,
        'current_date': current_date,
        'is_rainy': is_rainy,
        'is_sunny': is_sunny,
        'user_greeting': f"{greeting}, {request.user.firstname}",
    }
    
    return render(request, 'Dashboard/User-dashboard.html', context)

@login_required(login_url='login')
def admin_dashboard(request):
    total_employees = str(EmploymentInformation.objects.filter(name__is_active=True).exclude(name__is_admin=True).count()).zfill(4)
    regular = str(EmploymentInformation.objects.filter(name__is_active=True, Status__name="Regular").exclude(name__is_admin=True).count()).zfill(3)
    OJT = str(EmploymentInformation.objects.filter(name__is_active=True, Status__name="OJT").exclude(name__is_admin=True).count()).zfill(3)
    announcements = Announcements.objects.all().order_by('-posted_at')

    context={
        'total_employees':total_employees,
        'regular':regular,
        'OJT':OJT,
        'announcements':announcements
    }
    return render(request, 'Dashboard/admin-dashboard.html', context)


def weather_view(request):
    api_key = '1e7a89c02670496fb31233531241410'
    city = 'Biñan, Laguna'  # Set your city here
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

    # Fetch weather data from WeatherAPI
    response = requests.get(url)
    weather_data = response.json()
    
    # Determine if it's rainy or sunny based on weather description
    weather_condition = weather_data['current']['condition']['text'].lower()
    is_rainy = 'rain' in weather_condition
    is_sunny = 'sun' in weather_condition or 'clear' in weather_condition

    # Determine greeting based on time of day and weather condition
    current_time = timezone.localtime()
    if current_time.hour < 12:
        greeting = "Good morning" if is_sunny else "Rainy Morning"
    elif 12 <= current_time.hour < 18:
        greeting = "Good afternoon" if is_sunny else "Rainy Afternoon"
    else:
        greeting = "Good evening" if is_sunny else "Rainy Evening"
    
    context = {
        'is_rainy': is_rainy,
        'is_sunny': is_sunny,
        'greeting': f"{greeting}, Zen",
    }
    
    return render(request, 'Dashboard/User-dashboard.html', context)