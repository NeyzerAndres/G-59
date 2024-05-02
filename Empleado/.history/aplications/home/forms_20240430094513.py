from django import forms
from . import models

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = models.Prueba
        fields = ('titulo','subtitulo',)
        widgets = {
                'titulo':forms.TextInput(
                    attrs={'placeholder':'Ingrese el Titulo'}
                )
                }    

        
    def clean_titulo(self):
        validar = self.cleaned_data['titulo']
        print(len(validar))
        if len(validar) <= 2:
            raise forms.ValidationError('Ingrese un valor correcto')
        return validar
    
class c(forms.ModelForm):
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        
    
