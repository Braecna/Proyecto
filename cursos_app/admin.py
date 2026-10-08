from django.contrib import admin
from rest_framework import serializers

# Register your models here.
from .models import curso
from .models import encargado_curso
from .models import categoria
from .models import Inscripcion
from .models import contenido_curso
from .models import pais
from .models import Idioma

class cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = curso
        fields = '__all__'

class encargado_cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = encargado_curso
        fields = '__all__'
class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class contenido_cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = contenido_curso
        fields = '__all__'

class paisSerializer(serializers.ModelSerializer):
    class Meta:
        model = pais
        fields = '__all__'

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'
