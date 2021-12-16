from django.shortcuts import render
from rest_framework import viewsets
from .serializers import*
from .models import*
from .forms import*
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

def home(request):
    singerqueryset = Singer.objects.all()
    songqueryset = Song.objects.all()
    return render(request, 'basic.html', {'singers':singerqueryset, 'songs':songqueryset})

def Singer_Add(request):
    if request.method == "POST":
        form_data = SingerAdd(request.POST)
        if form_data.is_valid():
            # if u want to save cleaned data means one by one then use below method
            # name = form_data.cleaned_data['name']
            # gender = form_data.cleaned_data['gender']
            # var = Singer(name=name, gender=gender)
            # var.save()
            form_data.save()

    else:
        form_data = SingerAdd()
    return render(request, 'home.html',{'form':form_data} )

class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes=[UserRateThrottle, AnonRateThrottle]

class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    throttle_classes=[UserRateThrottle, AnonRateThrottle]

