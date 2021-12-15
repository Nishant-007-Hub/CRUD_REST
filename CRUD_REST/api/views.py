from django.shortcuts import render
from rest_framework import viewsets
from .serializers import*
from .models import*
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes=[UserRateThrottle,AnonRateThrottle]

class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

