from django.shortcuts import render, redirect
from .forms import addalbum
from .models import Album
# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = addalbum(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
    else:
        album_form = addalbum()
    return render(request,'album.html',{'form':album_form})

def edit_album(request,id):
    album = Album.objects.get(pk=id)
    album_form = addalbum(instance=album)
    if request.method == 'POST':
        album_form = addalbum(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
        
    return render(request,'album.html',{'form':album_form})

def delete_album(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home_page')