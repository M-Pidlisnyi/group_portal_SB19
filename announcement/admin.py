from django.contrib import admin
from .models import Announcement, Role, UserProfile

# Register your models here.

admin.site.register(Announcement)
admin.site.register(UserProfile)
admin.site.register(Role)