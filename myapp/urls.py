from django.conf.urls import url
from django.urls import path, include
from . import views


from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"programadores/?", views.ProgramadorView)



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('musics/', views.MusicList.as_view(), name='music-list'),
    #path('programador/', views.ProgramadorList.as_view(), name='programador-list'),
    path('programador/', include(router.urls), name='programador-list'),
    
]