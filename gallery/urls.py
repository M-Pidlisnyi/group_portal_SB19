from django.urls import path


from . import views
urlpatterns = [
    path("media/list/", views.double_list, "media-list"),
    path("photo/create", views.PhotoCreateView, "photo-create"),
    path("photo/edit/<int:pk>", views.PhotoEditView, "photo-edit"),
    path("photo/delete/<int:pk>", views.PhotoDeleteView, "photo-delete"),
    path("video/create/",  views.VideoCreateView, "video-create"),
    path("video/edit/<int:pk>", views.VideoEditView, "video-edit"),
    path("video/delete/<int:pk>",views.VideoDeleteView, "video-delete")
]