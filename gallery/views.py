from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

from .models import Photo, Video

def double_list(request:HttpRequest):
    first_list = Photo.objects.filter(photo="")
    second_list = Video.objects.all()

    return render(request, "gallery, media_list.html")

class PhotoCreateView(CreateView):
    model = Photo
    template_name = "gallery/photo_create.html"
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
class PhotoEditView(UpdateView,UserIsOwnerMixin):
    