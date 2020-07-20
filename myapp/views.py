from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Music, Programador
from .serializers import MusicSerializer,ProgramadorSerializer
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response

# Create your views here.
class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer


#class ProgramadorList(generics.ListCreateAPIView):
#
#    queryset = Programador.objects.all()
#    serializer_class = ProgramadorSerializer
#class ProgramadorView(APIView):
#    serializer_class = ProgramadorSerializer
#    def get(self,request):
#        dados = {}
#        programadores = Programador.objects.all()
#        print("<>",programadores)
#        dados['dados'] = programadores
#        return Response(dados,status=status.HTTP_200_OK)




class ProgramadorView(viewsets.ModelViewSet):

    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer

    def get_queryset(self):
        nome = self.request.query_params.get('nome',None)
        liguagem_atualmente = self.request.query_params.get('liguagem_atualmente',None)

        if nome or liguagem_atualmente:
            programador = Programador.objects.filter(nome__icontains=nome,liguagem_atualmente__icontains=liguagem_atualmente)
            return programador

        programador = Programador.objects.filter()
        return programador 


class Home(TemplateView):
    template_name = "home.html"