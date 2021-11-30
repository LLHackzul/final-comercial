from django.shortcuts import render, get_object_or_404, redirect
from .models import Mantenimiento
from .forms import MantenimientoForm


def mantenimiento_list(request):
    mantenimiento = Mantenimiento.objects.all()
    return render(request, 'hostpital/mantenimiento_list.html', {'mantenimientos': mantenimiento})

def new_mantenimiento(request):
    if request.method == "POST":
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            Mantenimiento = form.save(commit=False)
            Mantenimiento.save()
            return redirect('mantenimiento_list')
    else:
        form= MantenimientoForm()
    return render(request, 'hostpital/new_mantenimiento.html',{'form': form})

def mantenimiento_edit(request, pk):
    mant = get_object_or_404(Mantenimiento, pk=pk)
    if request.method == "POST":
        form = MantenimientoForm(request.POST, instance=mant)
        if form.is_valid():
            mant = form.save(commit=False)
            mant.save()
            return redirect('mantenimiento_list')
    else:
        form = MantenimientoForm(instance=mant)
    return render(request, 'hostpital/mantenimiento_edit.html', {'form': form})
def mantenimiento_remove(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    mantenimiento.delete()
    return redirect('mantenimiento_list')