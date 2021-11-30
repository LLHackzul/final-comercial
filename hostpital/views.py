from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctores, Mantenimiento,Pacientes, Anestesia, Assistant
from .forms import DoctoresForm, MantenimientoForm, PacientesForm, AnestesiaForm, AssistantForm


def list_Assistant(request):
    assist = Assistant.objects.all()
    return render(request, 'hostpital/list_Assistant.html', {'Enfermeria': assist})

def new_Assistant(request):
    if request.method == "POST":
        form = AssistantForm(request.POST)
        if form.is_valid():
            assist= form.save(commit=False)
            assist.save()
    else:
        form= AssistantForm()
    return render(request, 'hostpital/new_Assistant.html',{'form': form})

def edit_Assistant(request, pk):
    assist = get_object_or_404(Assistant, pk=pk)
    if request.method == "POST":
        form = AssistantForm(request.POST, instance=assist)
        if form.is_valid():
            assist = form.save(commit=False)
            assist.save()
            return redirect('list_Assistant')
    else:
        form = AssistantForm(instance=assist)
    return render(request, 'hostpital/edit_Assistant.html', {'form': form})

def remove_Assistant(request, pk):
    assist = get_object_or_404(Assistant, pk=pk)
    assist.delete()
    return redirect('list_Assistant')


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


def doctor_list(request):
    doctor = Doctores.objects.all()
    return render(request, 'hostpital/doctor_list.html', {'doctoress': doctor})

def new_doctor(request):
    if request.method == "POST":
        form = DoctoresForm(request.POST)
        if form.is_valid():
            Doctores = form.save(commit=False)
            Doctores.save()
            return redirect('doctor_list')
    else:
        form= DoctoresForm()
    return render(request, 'hostpital/new_doctor.html',{'form': form})

def doctor_edit(request, pk):
    doc = get_object_or_404(Doctores, pk=pk)
    if request.method == "POST":
        form = DoctoresForm(request.POST, instance=doc)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.save()
            return redirect('doctor_list')
    else:
        form = DoctoresForm(instance=doc)
    return render(request, 'hostpital/doctor_edit.html', {'form': form})
def doctor_remove(request, pk):
    doctor = get_object_or_404(Doctores, pk=pk)
    doctor.delete()
    return redirect('doctor_list') 


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
