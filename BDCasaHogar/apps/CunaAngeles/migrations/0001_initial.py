# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-20 21:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('lugar', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('patrocinadores', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Expendiente_escolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolaridad', models.CharField(max_length=60)),
                ('tutor', models.CharField(max_length=60)),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Expendiente_medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=48)),
                ('alergia', models.CharField(max_length=48)),
                ('altura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('enfermedades_hereditarias', models.CharField(max_length=48)),
                ('discapacidad', models.CharField(max_length=48)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fechaRegistrada', models.DateField(null=True)),
                ('fechaCaducacion', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(18)])),
                ('fechaNaci', models.DateField()),
                ('fechaRegis', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
                ('solicitud', models.CharField(max_length=60)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='expendiente_medico',
            name='nino',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CunaAngeles.Nino'),
        ),
        migrations.AddField(
            model_name='expendiente_escolar',
            name='nino',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CunaAngeles.Nino'),
        ),
    ]