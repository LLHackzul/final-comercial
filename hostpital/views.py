from django.http import request
from django.shortcuts import render, get_object_or_404, redirect

from .models import Anestesia
from .forms import AnestesiaForm

def anestesia_list(request):
    anestesia = Anestesia.objects.all()
    return render(request, 'hostpital/anestesia_list.html', {'anestesia': anestesia})

def new_anestesia(request):
    if request.method == "POST":
        form = AnestesiaForm(request.POST)
        if form.is_valid():
            Anestesia = form.save(commit=False)
            Anestesia.save()
            return redirect('anestesia_list')
    else:
        form= AnestesiaForm()
    return render(request, 'hostpital/new_anestesia.html',{'form': form})


def anestesia_edit(request, pk):
    mant = get_object_or_404(Anestesia, pk=pk)
    if request.method == "POST":
        form = AnestesiaForm(request.POST, instance=mant)
        if form.is_valid():
            mant = form.save(commit=False)
            mant.save()
            return redirect('anestesia_list')
    else:
        form = AnestesiaForm(instance=mant)
    return render(request, 'hostpital/anestesia_edit.html', {'form': form})

def anestesia_remove(request, pk):
    anestesia = get_object_or_404(Anestesia, pk=pk)
    anestesia.delete()
    return redirect('anestesia_list')

def inicio(request):
    return render( request, 'hostpital/index.html')