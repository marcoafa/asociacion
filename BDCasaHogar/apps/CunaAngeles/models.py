from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Nino(models.Model):
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(18)], null=True)
	fechaNaci = models.DateField()
	fechaRegis = models.DateField()

	def __unicode__(self):
		return self.nombre

class Eventos(models.Model):
	nombre = models.CharField(max_length=60)
	lugar = models.CharField(max_length=60)
	fecha = models.DateField()
	hora = models.TimeField()
	patrocinadores = models.CharField(max_length=60)

	def __unicode__(self):
		return 'nombre: %s - lugar: %s'%(self.nombre,self.lugar)

class Inventario(models.Model):
	nombre = models.CharField(max_length=60)
	fechaRegistrada = models.DateField(null=True)
	fechaCaducacion = models.DateField(null=True)

	def __unicode__(self):
		return 'nombre: %s'%(self.nombre)


class Solicitudes(models.Model):
	nombre = models.CharField(max_length=60)	
	correo = models.EmailField(null=False)
	solicitud = models.CharField(max_length=60)
	comentario = models.TextField()

	def __unicode__(self):
		return 'nombre: %s'%(self.nombre)


class Expendiente_escolar(models.Model):
	nino = models.OneToOneField(Nino)
	escolaridad = models.CharField(max_length=60)
	tutor = models.CharField(max_length=60)
	hora_entrada = models.TimeField()
	hora_salida = models.TimeField()
	comentario = models.TextField()
	

	def __unicode__(self):	
			return 'nino: %s'%(self.nino.name)

class Expendiente_medico(models.Model):
	nino = models.OneToOneField(Nino)
	doctor = models.CharField(max_length=48)
	alergia = models.CharField(max_length=48)
	altura = models.IntegerField()
	peso = models.IntegerField()
	edad = models.IntegerField()
	enfermedades_hereditarias = models.CharField(max_length=48)
	discapacidad = models.CharField(max_length=48)
	comentario = models.TextField()
	
	def __unicode__(self):	
		return 'nino: %s'%(self.nino.name)