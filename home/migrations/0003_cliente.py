# Generated by Django 4.1.2 on 2022-10-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_vahiculo_vehiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('domicilio', models.CharField(max_length=40)),
            ],
        ),
    ]
