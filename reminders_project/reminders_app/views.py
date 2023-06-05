from django.http import HttpResponse
from django.shortcuts import render
from .models import Reminder

def index(request):
    return render(request, 'index.html')

def get_reminders(request):
    reminders = Reminder.objects.all()
    # Convert reminders to JSON and return as HttpResponse
    return HttpResponse(reminders, content_type='application/json')


