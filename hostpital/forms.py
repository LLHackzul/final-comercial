from django import forms

from .models import Anestesia

class AnestesiaForm(forms.ModelForm):

    class Meta:
        model = Anestesia
        fields = ('cui', 'firstName', 'secondName', 'firstSurname','secondSurname', 'number', 'email')