from django.contrib import admin
from .models import Nino, Eventos, Inventario, Solicitudes, Expendiente_medico, Expendiente_escolar

admin.site.register(Nino)
admin.site.register(Eventos)
admin.site.register(Inventario)
admin.site.register(Expendiente_medico)
admin.site.register(Expendiente_escolar)

@admin.register(Solicitudes)
class Solicitudes_admin(admin.ModelAdmin):
	list_display = ('nombre','solicitud','comentario',)