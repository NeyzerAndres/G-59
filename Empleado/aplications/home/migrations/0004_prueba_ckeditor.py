# Generated by Django 5.0.4 on 2024-05-08 18:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='ckeditor',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
