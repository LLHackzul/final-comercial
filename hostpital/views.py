from django.shortcuts import render, get_object_or_404, redirect
from .models import Pacientes
from .forms import PacientesForm

def paciente_list(request):
    paciente = Pacientes.objects.all()
    return render(request, 'hostpital/paciente_list.html',{'pacientes':paciente})

def new_paciente(request):
    if request.method == "POST":
        form = PacientesForm(request.POST)
        if form.is_valid():
            Paciente = form.save(commit=False)
            Paciente.save()
            return redirect('paciente_list')
    else:
        form= PacientesForm()
    return render(request, 'hostpital/new_paciente.html',{'form': form})

def paciente_edit(request, pk):
    pa= get_object_or_404(Pacientes, pk=pk)
    if request.method== "POST":
        form = PacientesForm(request.POST, instance=pa)
        if form.is_valid():
            pa = form.save(commit=False)
            pa.save()
            return redirect('paciente_list')
    else:
        form= PacientesForm(instance=pa)
    return render(request, 'hostpital/paciente_edit.html',{'form': form})

def paciente_remove(request, pk):
    paciente= get_object_or_404(Pacientes, pk=pk)
    paciente.delete()
    return redirect('paciente_list')