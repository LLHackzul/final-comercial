from django import forms

from .models import Doctores

class DoctoresForm(forms.ModelForm):

    class Meta:
        model = Doctores
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email')