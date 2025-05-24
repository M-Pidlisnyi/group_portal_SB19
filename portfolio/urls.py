from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('create/', views.portfolio_create, name='portfolio_create'),
    path('edit/<int:pk>/', views.portfolio_edit, name='portfolio_edit'),
    path('delete/<int:pk>/', views.portfolio_delete, name='portfolio_delete'),
]