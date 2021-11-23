from django import forms

from .models import Pacientes

class PacientesForm(forms.ModelForm):

    class Meta:
        model = Pacientes
        fields = ('historyNumber', 'firstName', 'secondName', 'firtSurname','secondSurname', 'age', 'gender')