from django import forms

from .models import Doctores, Mantenimiento

class DoctoresForm(forms.ModelForm):

    class Meta:
        model = Doctores

class MantenimientoForm(forms.ModelForm):

    class Meta:
        model = Mantenimiento
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email')