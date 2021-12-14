from django.db.models import fields
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from CRUD_REST.api.models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'
