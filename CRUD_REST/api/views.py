from django.shortcuts import redirect, render
from rest_framework import viewsets
from .serializers import*
from .models import*
from .forms import*
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


def home(request):
    singerqueryset = Singer.objects.all()
    songqueryset = Song.objects.all()
    return render(request, 'basic.html', {'singers':singerqueryset, 'songs':songqueryset})


def Singerr_Add(request):
    if request.method == "POST":
        form_data_singer = SingerAdd(request.POST)
        form_data_song = SongAdd(request.POST)
        if form_data_singer.is_valid():
            # if u want to save cleaned data means one by one then use below method
            # if u want to leave any field balnk during save so use below method
            # name = form_data_singer.cleaned_data['name']
            # gender = form_data_singer.cleaned_data['gender']
            # var = Singer(name=name, gender=gender)
            # var.save()
            form_data_singer.save()
            form_data_singer = SingerAdd()
        if form_data_song.is_valid():
            # title = form_data_song.cleaned_data['title']
            # singer = form_data_song.cleaned_data['singer']
            # var = Song(title=title, singer=singer)
            # var.save()
            form_data_song.save()
            # below is for after save, u will see blank form on frontend we are initializing blank form
            form_data_song = SongAdd()

    else:
        form_data_singer = SingerAdd()
        form_data_song = SongAdd()
    singer = Singer.objects.all()
    song = Song.objects.all()
    return render(request, 'home2.html',{'form_singer':form_data_singer, 'form_song': form_data_song , 'singers':singer, 'songs':song})

def delete_data_song(request, slug):
    if request.method == 'POST':
        deleteset_song = Song.objects.get(title=slug)
        deleteset_song.delete()
        return redirect('/')

def delete_data_singer(request, myid):
    if request.method == 'POST':
        deleteset = Singer.objects.get(pk=myid)
        deleteset.delete()
        return redirect('/')


def edit_data_singer(request, myid):
    if request.method == "POST":
        editset = Singer.objects.get(pk=myid)
        var = SingerAdd(request.POST, instance=editset)
        if var.is_valid():
            var.save()
            var = SingerAdd()
            return redirect('/')
    else:
        editset = Singer.objects.get(pk=myid)
        var = SingerAdd(instance=editset)
    return render(request, 'updatesinger.html', {'var':var})

def edit_data_song(request, slug):
    if request.method == "POST":
        editset = Song.objects.get(title=slug)
        var = SongAdd(request.POST, instance=editset)
        if var.is_valid():
            var.save()
            var = SongAdd()
            return redirect('/')
    else:
        editset = Song.objects.get(title=slug)
        var = SongAdd(instance=editset)
    return render(request, 'updatesong.html', {'var':var})


# def Singer_Add(request):
#     if request.method == "POST":
#         form_data = SingerAdd(request.POST)
#         if form_data.is_valid():
#             # if u want to save cleaned data means one by one then use below method
#             # if u want to leave any field balnk during save so use below method
#             # name = form_data.cleaned_data['name']
#             gender = form_data.cleaned_data['gender']
#             # var = Singer(name=name, gender=gender)
#             # var.save()
#             form_data.save()
#             # below is for after save, u will see blank form on frontend we are initializing blank form
#             form_data = SingerAdd()

#     else:
#         form_data = SingerAdd()
#     singer = Singer.objects.all()
#     return render(request, 'home.html',{'form':form_data, 'singers':singer})


    
# def Song_Add(request):
#     if request.method == "POST":
#         form_data = SongAdd(request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             # below is for after save, u will see blank form on frontend we are initializing blank form
#             form_data = SongAdd()

#     else:
#         form_data = SongAdd()
#     songs = Song.objects.all()
#     return render(request, 'home.html',{'form':form_data, 'songs':songs})

# def delete_data(request, myid):
#     if request.method == 'POST':
#         deleteset = Singer.objects.get(pk=myid)
#         deleteset.delete()
#         return redirect('/add')

# def edit_data(request, myid):
#     if request.method == "POST":
#         editset = Singer.objects.get(pk=myid)
#         var = SingerAdd(request.POST, instance=editset)
#         if var.is_valid():
#             var.save()
#             var = SingerAdd()
#     else:
#         editset = Singer.objects.get(pk=myid)
#         var = SingerAdd(instance=editset)
#     return render(request, 'updatesinger.html', {'var':var})
     


class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes=[UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','singer']

    # def get_queryset(self):
    #     # gender = self.request.gender
    #     return Singer.objects.filter(gender='male')

class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    throttle_classes=[UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name'] 

