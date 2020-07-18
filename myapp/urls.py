from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('musics/', views.MusicList.as_view(), name='music-list'),
    path('programador/', views.ProgramadorList.as_view(), name='programador-list'),
]