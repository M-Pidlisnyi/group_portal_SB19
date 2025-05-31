from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
class Announcement(models.Model):
    title = models.CharField( max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField("auth.Permission")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        from .models import UserProfile, Role
        default_role, _ = Role.objects.get_or_create(name='User')
        UserProfile.objects.create(user=instance, role=default_role)