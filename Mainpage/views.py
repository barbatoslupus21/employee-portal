from django.shortcuts import render, redirect

def mainpage(request):
    return render(request, 'Mainpage/homepage.html')
