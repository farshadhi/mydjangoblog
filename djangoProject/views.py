# for running a project write this statement into terminal: 'python manage.py runserver'
from django.shortcuts import render
from django.shortcuts import HttpResponse
# def mainpage(request):
#     return HttpResponse('اولین صفحه‌ی من')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')