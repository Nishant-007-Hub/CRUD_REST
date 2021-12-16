from django.shortcuts import redirect, render
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
            # if u want to leave any field balnk during save so use below method
            # name = form_data.cleaned_data['name']
            gender = form_data.cleaned_data['gender']
            # var = Singer(name=name, gender=gender)
            # var.save()
            form_data.save()
            # below is for after save, u will see blank form on frontend we are initializing blank form
            form_data = SingerAdd()

    else:
        form_data = SingerAdd()
    singer = Singer.objects.all()
    return render(request, 'home.html',{'form':form_data, 'singers':singer})

def delete_data(request, myid):
    if request.method == 'POST':
        deleteset = Singer.objects.get(pk=myid)
        deleteset.delete()
        return redirect('/add')

def edit_data(request, myid):
    if request.method == "POST":
        editset = Singer.objects.get(pk=myid)
        var = SingerAdd(request.POST, instance=editset)
        if var.is_valid():
            var.save()
    else:
        editset = Singer.objects.get(pk=myid)
        var = SingerAdd(instance=editset)
    return render(request, 'updatesinger.html', {'var':var})


class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes=[UserRateThrottle, AnonRateThrottle]

class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    throttle_classes=[UserRateThrottle, AnonRateThrottle]

