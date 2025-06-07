from django.urls import path
from . import views
urlpatterns = [
    path("", views.MaterialListView.as_view(), name="material-list"),
    path("material/create/", views.MaterialCreateView.as_view(), name="material-create"),
    path("material/list/", views.MaterialListView.as_view(), name="material-list"),
    path("material/detail/<int:pk>", views.MaterialDetailView.as_view(), name="material-detail"),
    path("material/edit/<int:pk>", views.MaterialEditView.as_view(), name="material-edit"),
    path("material/delete/<int:pk>", views.MaterialDeleteView.as_view(), name="material-delete"),  
]