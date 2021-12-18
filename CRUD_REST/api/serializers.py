from django.db.models import fields
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    sung_by = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = '__all__' 
