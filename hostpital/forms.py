from django import forms
from .models import Doctores, Mantenimiento, Pacientes, Anestesia

class AnestesiaForm(forms.ModelForm):

    class Meta:
        model = Anestesia
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email')


class PacientesForm(forms.ModelForm):

    class Meta:
        model = Pacientes
        fields = ('historyNumber', 'firstName', 'secondName', 'firtSurname','secondSurname', 'age', 'gender')

class DoctoresForm(forms.ModelForm):

    class Meta:
        model = Doctores
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email')
class MantenimientoForm(forms.ModelForm):

    class Meta:
        model = Mantenimiento
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email')

