# Generated by Django 4.1.2 on 2022-11-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionusuario',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='extensionusuario',
            name='link_pagina',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
