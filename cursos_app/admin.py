from django.contrib import admin
from .models import curso
from .models import encargado_curso
from .models import categoria
from .models import Inscripcion
from .models import contenido_curso
from .models import pais
from .models import Idioma


# Register your models here.
admin.site.register(curso)
admin.site.register(encargado_curso)
admin.site.register(categoria)
admin.site.register(Inscripcion)
admin.site.register(contenido_curso)
admin.site.register(pais)
admin.site.register(Idioma)
