from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

from gallery.forms import CreateupdatePhotoForm, CreateupdateVideoForm
from gallery.mixins import UserIsOwnerMixin

from .models import Photo, Video

def double_list(request:HttpRequest):
    first_list = Photo.objects.filter(photo="")
    second_list = Video.objects.all()

    context = {
        "all_media":first_list+second_list

    }

    return render(request, "gallery, media_list.html")

class PhotoCreateView(CreateView):
    model = Photo
    template_name = "gallery/photo_create.html"
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
class PhotoEditView(UpdateView,UserIsOwnerMixin):
    model = Photo
    form_class = CreateupdatePhotoForm
    template_name = "gallery/photo_create.html"
    success_url = reverse_lazy("media-list")
class PhotoDeleteView(DeleteView, UserIsOwnerMixin):
    model = Photo
    success_url = reverse_lazy("media-list")
class VideoCreateView(CreateView):
    model = Video
    template_name = "gallery/video_create.html"
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
class VideoEditView(UpdateView,UserIsOwnerMixin):
    model = Video
    form_class = CreateupdateVideoForm
    template_name="gallery/video_create.html"
    success_url = reverse_lazy("media-list")
class VideoDeleteView(DeleteView, UserIsOwnerMixin):
    model = Video
    success_url = reverse_lazy("media-list")