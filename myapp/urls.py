from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('musics/', views.MusicList.as_view(), name='music-list'),
    path('/', views.ProgramadorList.as_view(), name='programador-list'),
]