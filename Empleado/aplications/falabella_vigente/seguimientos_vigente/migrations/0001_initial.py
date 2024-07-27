# Generated by Django 5.0.4 on 2024-06-04 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tabla_Prueba',
                'verbose_name_plural': 'Tabla_Pruebas',
            },
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimientos_vigente.prueba')),
            ],
            options={
                'verbose_name': 'Tabla_Relacion',
                'verbose_name_plural': 'Tabla_Relaciones',
            },
        ),
    ]
