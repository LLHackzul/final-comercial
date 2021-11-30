from django import forms

from .models import Doctores, Mantenimiento, Pacientes, Anestesia, Assistant

class AssistantForm(forms.ModelForm):

    class Meta:
        model = Assistant
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email', 'AssistType')


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

