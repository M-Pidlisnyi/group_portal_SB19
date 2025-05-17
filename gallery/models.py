from django.db import models
from django.contrib.auth.models import User

class Student(models.BaseModel):
    name = models.CharField(max_length=100)
class Photo(models.BaseModel):
    photo = models.ImageField(upload_to="", blank=True, null=True)
class Video(models.BaseModel):
    video = models.FileField(upload_to="", blank=True, null=True)