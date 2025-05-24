from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
class Photo(models.Model):
    photo = models.ImageField(upload_to="", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField()
    class Meta:
        verbose_name = "photos"
class Video(models.Model):
    video = models.FileField(upload_to="", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    uploaded_at = models.DateTimeField()
    class Meta:
        verbose_name = "videos"