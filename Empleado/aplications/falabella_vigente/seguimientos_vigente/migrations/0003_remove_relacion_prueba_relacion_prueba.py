# Generated by Django 5.0.4 on 2024-06-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimientos_vigente', '0002_alter_prueba_estado_alter_relacion_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relacion',
            name='prueba',
        ),
        migrations.AddField(
            model_name='relacion',
            name='prueba',
            field=models.ManyToManyField(to='seguimientos_vigente.prueba'),
        ),
    ]
