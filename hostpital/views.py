from django.shortcuts import render
from .forms import MantenimientoForm

def new_mantenimiento(request):
    if request.method == "POST":
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            Mantenimiento = form.save(commit=False)
            Mantenimiento.save()
    else:
        form= MantenimientoForm()
    return render(request, 'hostpital/new_mantenimiento.html',{'form': form})