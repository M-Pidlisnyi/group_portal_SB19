from django.shortcuts import render, get_object_or_404, redirect
from .models import Announcement
from .forms import AnnouncementForm
from django.db.models import Q
def announcements_list(request):
    announcements = Announcement.objects.order_by('-created_at')
    return render(request, 'announcements/list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'announcements/detail.html', {'announcement': announcement})

def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            new_announcement = form.save()
            return redirect('announcement_detail', pk=new_announcement.pk)
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/form.html', {'form': form})

def announcement_edit(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_detail', pk=pk)
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcements/form.html', {'form': form})

def announcement_delete(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcements_list')
    return render(request, 'announcements/confirm_delete.html', {'announcement': announcement})

def announcements_search(request):
    query = request.GET.get('q', '')
    announcements = Announcement.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).order_by('-created_at')
    return render(request, 'announcements/search_results.html', {'announcements': announcements, 'query': query})