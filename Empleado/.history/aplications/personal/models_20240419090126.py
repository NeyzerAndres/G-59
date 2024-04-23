from django.shortcuts import render
from models import MiModelo
import pandas as pd  # Necesitarás instalar pandas (pip install pandas)

def cargar_archivo(request):
    if request.method == 'POST' and request.FILES['archivo_xlsx']:
        archivo = request.FILES['archivo_xlsx']
        df = pd.read_excel(archivo)  # Lee el archivo XLSX con pandas
        for index, row in df.iterrows():
            # Crea un objeto de modelo y guarda los datos en la base de datos
            MiModelo.objects.create(nombre=row['Nombre'], edad=row['Edad'], ...)  # Agrega los campos según tu modelo
        return render(request, 'exito.html')  # Redirige a una página de éxito
    return render(request, 'upload_form.html')
