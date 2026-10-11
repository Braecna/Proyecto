from django.db import models
from django.conf import settings
# Create your models here.

class categoria(models.Model):
    categoria_id= models.AutoField(primary_key=True)
    n_categoria = models.CharField(max_length=100, null=False)
    class Meta:
        db_table_comment = "Tabla de categorias de cursos"

class encargado_curso(models.Model):
    encargado_id= models.AutoField(primary_key=True)
    profesor =models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='username')
    class Meta:
        db_table_comment = "Tabla de encargados de cursos"

class curso(models.Model):
    curso_id= models.AutoField(primary_key=True)
    n_curso = models.CharField(max_length=100, null=False)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=False)
    fecha_termino = models.DateField(null=False)
    valor_curso = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descripcion = models.TextField(null=False)
    encargado = models.ForeignKey(encargado_curso, on_delete=models.CASCADE, db_column='profesor')
    class Meta:
        db_table_comment = "Tabla de cursos"

class Inscripcion(models.Model):
    inscripcion_id= models.AutoField(primary_key=True)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE, db_column='n_curso')
    usuario=models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='username')
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, null=False)
    class Meta:
        db_table_comment = "Tabla de inscripciones a cursos"

class contenido_curso(models.Model):
    contenido_id= models.AutoField(primary_key=True)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE, db_column='n_curso')
    titulo = models.CharField(max_length=100, null=False) 
    descripcion = models.TextField(null=False)
    class Meta:
        db_table_comment = "Tabla de contenidos de cursos"

class pais(models.Model):
    pais_id= models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=100, null=False)
    class Meta:
        db_table_comment = "Tabla de paises"

class region(models.Model):
    region_id= models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100, null=False)
    pais = models.ForeignKey(pais,on_delete=models.PROTECT,related_name='regiones')
    class Meta:
        db_table_comment = "Tabla de regiones"

class provincia(models.Model):
    provincia_id= models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100, null=False)
    region=models.ForeignKey(region,on_delete=models.PROTECT,related_name='provincias')
    habilitado = models.BooleanField(default=True,null=False)
    class Meta:
        db_table_comment = "Tabla de provincias"

class Idioma(models.Model):
    idioma_id= models.AutoField(primary_key=True)
    nombre_idioma = models.CharField(max_length=100, null=False)
    class Meta:
        db_table_comment = "Tabla de idiomas"

class clientes(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="cliente",)
    direccion = models.CharField(max_length=100, null=False)
    numero_domicilio = models.CharField(max_length=20, null=False)
    provincia = models.ForeignKey(provincia, on_delete=models.PROTECT, related_name='clientes')
    telefono = models.CharField(max_length=20, null=False)
    class Meta:
        db_table_comment = "Tabla de clientes"
