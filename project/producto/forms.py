from django import forms

from . import models

class provedorForm(forms.ModelForm):
    class Meta:
        model= models.Provedor
        fields = ['nombre','contacto']
        