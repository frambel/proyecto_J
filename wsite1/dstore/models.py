# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# a decisiòn personal, còmo quieran cada modelo!

class Disquera(models.Model):
	nombre = models.CharField('Compañía', max_length = 30)
	domicilio = models.CharField('Dirección', max_length = 90, blank = True)
	ciudad = models.CharField(max_length = 30)
	estado = models.CharField(max_length = 30)
	pais = models.CharField('País', max_length = 30)
	sitioweb = models.URLField('Website', blank = True)

	class Meta: # Para poder ordenar las listas en el admin
		ordering = ["nombre", "pais"]
		verbose_name_plural = "Disqueras"

	def __unicode__(self):
		return self.nombre

class Artista(models.Model):
	artistico = models.CharField('Artista o Grupo', max_length = 90)
	nombre = models.CharField('Nombre(s)', max_length = 30, blank = True)
	apellido = models.CharField('Apellido(s)', max_length = 30, blank = True)
	instagram = models.CharField(max_length = 30, blank = True)
	twitter = models.CharField(max_length = 30, blank = True)
	artista = models.ImageField('Foto Artista', upload_to = 'foto_artista', null = True, blank = True)
	# se puede agregar por país 

	class Meta: # Para poder ordenar las listas en el admin
		ordering = ["artistico", "nombre", "apellido"]
		verbose_name_plural = "Artistas"

	def __unicode__(self):
		return self.artistico

class Disco(models.Model):
	titulo = models.CharField('Album', max_length = 90)
	artista = models.ManyToManyField(Artista, verbose_name = "Artista(s)")
	disquera = models.ForeignKey(Disquera)
	fecha_publicacion = models.DateField(null = True, blank = True, verbose_name = "Publicación")
	cover = models.ImageField('Cover Album', upload_to = 'foto_cover', null = True, blank = True)

	class Meta: # Para poder ordenar las listas en el admin
		ordering = ["titulo", "fecha_publicacion"]
		verbose_name_plural = "Discos"

	def __unicode__(self):
		return self.titulo