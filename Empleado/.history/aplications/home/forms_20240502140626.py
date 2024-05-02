from django import forms
from . import models

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = models.Prueba
        fields = ('titulo','subtitulo',)
        widgets = {'titulo':forms.TextInput(attrs={'placeholder':'Ingrese el Titulo'})}    

        
    def clean_titulo(self):
        validar = self.cleaned_data['titulo']
        print(len(validar))
        if len(validar) <= 2:
            raise forms.ValidationError('Ingrese un valor correcto')
        return validar
    



class PasswordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Esto eliminará 'user' de kwargs si está presente
        super(MyForm, self).__init__(*args, **kwargs)
        for field_name,field in self.visible_fields():
            field.widget.attrs['class'] = 'form-control'
    