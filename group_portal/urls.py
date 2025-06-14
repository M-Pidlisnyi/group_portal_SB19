"""
URL configuration for group_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forms.views import MarkList, MarkDetail, MarkCreate, MarkDelete, MarkEdit
urlpatterns = [
    path('admin/', admin.site.urls),
    path('marks/', MarkList.as_view(), name='marks'),
    path('mark/detail/<int:pk>/', MarkDetail.as_view(), name='mark-detail'),
    path('mark/create/', MarkCreate.as_view(), name='mark-create'),
    path('mark/delete/<int:pk>/', MarkDelete.as_view(), name='mark-delete'),
    path('mark/edit/<int:pk>/', MarkEdit.as_view(), name='mark-edit'),
    path("", include("material.urls")),
    path('', include('announcement.urls')),

]
