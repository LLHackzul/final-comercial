from django.shortcuts import render
from .forms import PacientesForm

def new_paciente(request):
    if request.method == "POST":
        form = PacientesForm(request.POST)
        if form.is_valid():
            Paciente = form.save(commit=False)
            Paciente.save()
    else:
        form= PacientesForm()
    return render(request, 'hostpital/new_paciente.html',{'form': form})