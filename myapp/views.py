from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Music,Programador
from .serializers import MusicSerializer,ProgramadorSerializer

# Create your views here.
class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class ProgramadorList(generics.ListCreateAPIView):

    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer