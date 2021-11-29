from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctores
from .forms import DoctoresForm


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