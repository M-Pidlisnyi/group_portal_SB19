from django.shortcuts import render
from .models import Announcement
# Create your views here.

def announcements_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements/list.html', {'announcements': announcements})
