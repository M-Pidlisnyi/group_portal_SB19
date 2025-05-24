from django.urls import path


from . import views
urlpatterns = [
    "/media/list/", views.double_list, "media-list"
]