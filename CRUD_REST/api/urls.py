"""CRUD_REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from .views import*
from rest_framework import routers

router = routers.DefaultRouter()

router.register('SongModelViewset', SongModelViewSet, basename='SongModelViewSet')
router.register('SingerModelViewset', SingerModelViewSet, basename='SingerModelViewSet')

urlpatterns = [
    path('', Singerr_Add, name='home'),
    # path('', Song_Add, name='home'),
    # path('', home, name='homeBasic'),
    path('delete/<int:myid>/', delete_data_singer, name='delete_data_singer'),
    path('delete/<slug>/', delete_data_song, name='delete_data_song'),
    path('<int:myid>/', edit_data_singer, name='edit_data_singer'),
    path('<slug>/', edit_data_song, name='edit_data_song'),
    path('api/', include(router.urls)),
]
