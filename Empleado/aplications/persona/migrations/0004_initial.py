# Generated by Django 4.1 on 2024-02-22 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0004_initial'),
        ('persona', '0003_alter_empleado_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=30, unique=True, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad de Empleado',
                'verbose_name_plural': 'Habilidades de los Empleados',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, unique=True, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Otro')], max_length=50, verbose_name='Trabajo')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='empleado')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
            options={
                'verbose_name': 'Mi empleado',
                'verbose_name_plural': 'Empleado en Departamentos',
                'ordering': ['departamento'],
                'unique_together': {('job', 'first_name')},
            },
        ),
    ]
