# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dstore.models import Disquera, Artista, Disco

# Clases para mostrar en el Admin

class DisqueraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'pais', 'sitioweb')
	search_fields = ('nombre', 'pais')


class ArtistaAdmin(admin.ModelAdmin):
	list_display = ('artistico', 'artista')
	search_fields = ('artistico', 'nombre', 'apellido')
	fields = ('artistico', 'artista', 'nombre', 'apellido', 'instagram', 'twitter')


class DiscoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'cover', 'fecha_publicacion')
	search_fields = ('titulo', 'artista', 'disquera')
	list_filter = ('fecha_publicacion',)
	date_hierarchy = 'fecha_publicacion'
	fields = ('titulo', 'cover', 'artista', 'fecha_publicacion', 'disquera')
	filter_horizontal = ('artista',)
	raw_id_fields = ('disquera',)


# Register your models here.
admin.site.register(Disquera, DisqueraAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Disco, DiscoAdmin)