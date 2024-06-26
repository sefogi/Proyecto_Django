# Generated by Django 5.0.4 on 2024-04-21 03:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutorDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=75, verbose_name='Nombre')),
                ('Fecha_nacimiento', models.DateField(verbose_name='Fecha nacimiento')),
                ('Fecha_fallecimiento', models.DateField(blank=True, null=True, verbose_name='Fecha fallecimiento')),
                ('Profesion', models.CharField(max_length=50, verbose_name='Profesion')),
                ('Nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='FraseDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cita', models.TextField(max_length=400, verbose_name='Cita')),
                ('Autor_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.autordb')),
            ],
        ),
    ]
