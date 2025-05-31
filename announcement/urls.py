from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.announcements_list, name='announcements_list'),
    path('create/', views.announcement_create, name='announcement_create'),
    path('search/', views.announcements_search, name='announcements_search'),  
    path('<int:pk>/', views.announcement_detail, name='announcement_detail'),
    path('edit/<int:pk>/', views.announcement_edit, name='announcement_edit'),
    path('delete/<int:pk>/', views.announcement_delete, name='announcement_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='announcements_list'), name='logout'),
]
