from django import forms

from .models import Mantenimiento

class MantenimientoForm(forms.ModelForm):

    class Meta:
        model = Mantenimiento
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email')