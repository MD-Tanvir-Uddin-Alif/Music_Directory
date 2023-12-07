from django.shortcuts import render,redirect
from .forms import AddMusician
from .models import Musician
# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        musician_form = AddMusician(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home_page')
    else:
        musician_form = AddMusician()
    return render(request,'musician.html',{'form' : musician_form})

def edit_musician(request,id):
    musician = Musician.objects.get(pk=id)
    musician_form = AddMusician(instance=musician)
    if request.method == 'POST':
        musician_form = AddMusician(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home_page')

    return render(request,'musician.html',{'form' : musician_form})