from django import forms

from . import models


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['nombre', 'apellido', 'nacimiento', 'pais_origen']
        labels = {'nombre': 'nombre', 'apellido': 'aéllido', 'nacimiento': 'nacimiento','pais_origen': 'pais_origen'}
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_origen': forms.TextInput(attrs={'class': 'form-control'})
            }
