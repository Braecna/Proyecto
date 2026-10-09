from rest_framework import serializers

from .models import curso, encargado_curso, categoria, Inscripcion, contenido_curso, pais, Idioma

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
