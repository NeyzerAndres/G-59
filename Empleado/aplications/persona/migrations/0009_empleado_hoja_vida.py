# Generated by Django 4.1 on 2024-03-07 10:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0008_habilidad_empleados_delete_habilidades_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
