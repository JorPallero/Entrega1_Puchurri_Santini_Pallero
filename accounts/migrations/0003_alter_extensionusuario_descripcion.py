# Generated by Django 4.1.2 on 2022-11-12 21:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_extensionusuario_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extensionusuario',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
