from django import forms

class NuevoDepartamento(forms.Form):
    nombre = forms.CharField(max_length=50)
    Apellido = forms.CharField(max_length=50)
    Departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)
    