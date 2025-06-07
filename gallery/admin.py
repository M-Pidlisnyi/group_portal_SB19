from django.contrib import admin

from .models import Photo, Student, Video


admin.site.register(Student)
admin.site.register(Photo)
admin.site.register(Video)