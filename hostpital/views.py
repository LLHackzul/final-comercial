from django.shortcuts import render

from hostpital.models import Assistant
from .forms import AssistantForm

def new_Assistant(request):
    if request.method == "POST":
        form = AssistantForm(request.POST)
        if form.is_valid():
            Assistant = form.save(commit=False)
            Assistant.save()
    else:
        form= AssistantForm()
    return render(request, 'hostpital/new_Assistant.html',{'form': form})