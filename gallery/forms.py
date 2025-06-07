from django import forms
from .models import Photo, Video


class CreateupdatePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        exclude = ["user"]
class CreateupdateVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
        exclude = ["user"]