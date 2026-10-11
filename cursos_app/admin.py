from django.contrib import admin
from .models import curso, encargado_curso, categoria, Inscripcion, contenido_curso, pais, region, Idioma, clientes, provincia


# Register your models here.
admin.site.register(curso)
admin.site.register(encargado_curso)
admin.site.register(categoria)
admin.site.register(Inscripcion)
admin.site.register(contenido_curso)
admin.site.register(pais)
admin.site.register(Idioma)
admin.site.register(region)
admin.site.register(clientes)
admin.site.register(provincia)
