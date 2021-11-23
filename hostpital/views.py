from django.shortcuts import render

from hostpital.models import Anestesia
from .forms import AnestesiaForm

def new_anestesia(request):
    if request.method == "POST":
        form = AnestesiaForm(request.POST)
        if form.is_valid():
            Anestesia = form.save(commit=False)
            Anestesia.save()
    else:
        form= AnestesiaForm()
    return render(request, 'hostpital/new_anestesia.html',{'form': form})
