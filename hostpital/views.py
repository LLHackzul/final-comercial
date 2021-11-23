from django.shortcuts import render

from hostpital.models import Doctores

# Create your views here.
from .forms import DoctoresForm

def new_doctor(request):
    if request.method == "POST":
        form = DoctoresForm(request.POST)
        if form.is_valid():
            Doctores = form.save(commit=False)
            Doctores.save()
    else:
        form= DoctoresForm()
    return render(request, 'hostpital/new_doctor.html',{'form': form})