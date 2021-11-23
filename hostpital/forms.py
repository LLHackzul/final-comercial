from django import forms

from .models import Assistant

class AssistantForm(forms.ModelForm):

    class Meta:
        model = Assistant
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email', 'AssistType')