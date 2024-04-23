from django.shortcuts import render
from miapp.models import 
import pandas as pd  # Necesitarás instalar pandas (pip install pandas)from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User

class PasswordResetRequestView(View):
    def get(self, request):
        return render(request, 'personal/reset_password.html')

    def post(self, request):
        email = request.POST.get('email')  # Suponiendo que obtienes el correo electrónico del formulario

        try:
            usuario = User.objects.get(username=email)  # Suponiendo que tienes un modelo de Usuario con un campo de correo electrónico
        except User.DoesNotExist:
            # Maneja el caso en el que el correo electrónico no esté asociado a ningún usuario
            return HttpResponse("No se encontró ningún usuario asociado a este correo electrónico.")

        # Genera un token único para el usuario
        token = default_token_generator.make_token(usuario)

        # Ahora puedes utilizar este token para crear el enlace de restablecimiento de contraseña y enviarlo al usuario

        return HttpResponse("Se ha enviado un enlace para restablecer la contraseña al usuario.")


class PasswordResetConfirmViewCustom(PasswordResetConfirmView):
    template_name = 'personal/reset_password_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class PasswordResetCompleteViewCustom(PasswordResetCompleteView):
    template_name = 'personal/reset_password_complete.html'
    
def cargar_archivo(request):
    if request.method == 'POST' and request.FILES['archivo_xlsx']:
        archivo = request.FILES['archivo_xlsx']
        df = pd.read_excel(archivo)  # Lee el archivo XLSX con pandas
        for index, row in df.iterrows():
            # Crea un objeto de modelo y guarda los datos en la base de datos
            MiModelo.objects.create(nombre=row['Nombre'], edad=row['Edad'], ...)  # Agrega los campos según tu modelo
        return render(request, 'exito.html')  # Redirige a una página de éxito
    return render(request, 'upload_form.html')
