from django.shortcuts import render
from rest_framework import viewsets
from .serializers import*
from .models import*

class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

