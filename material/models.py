from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class TypeMaterial(models.TextChoices):
    LINK = 'link', 'посилання'
    FILE = 'file', 'Файл' 
    IMAGE = 'image', "зображення" 
    YOUTUBE = "youtube", "youtube посилання"

class Material(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва")
    details = models.TextField(blank=True, verbose_name="Опис")
    type = models.CharField(max_length=15, choices=TypeMaterial.choices, verbose_name="Тип матеріала")
    link = models.URLField(null=True, blank=True, verbose_name="Посилання")
    y_link = models.URLField(null=True, blank=True, verbose_name="Посилання ютуб")
    file = models.FileField(upload_to="material/files", null= True, blank=True, verbose_name="Файл")
    image = models.ImageField(upload_to="material/image", null=True, blank=True, verbose_name="Зображення")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated = models.DateTimeField(auto_now=True, verbose_name="Оновлення")
    us = models.ForeignKey(User, null = True, verbose_name="Ким додано")

    def __str__(self):
        return self.name
    
    