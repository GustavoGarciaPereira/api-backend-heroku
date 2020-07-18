from rest_framework import serializers
from .models import Music, Programador

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class ProgramadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programador
        fields = '__all__'