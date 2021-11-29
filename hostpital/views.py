from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from hostpital.models import Assistant
from .forms import AssistantForm

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