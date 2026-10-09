from django.db import models

# Create your models here.

class categoria(models.Model):
    categoria_id= models.AutoField(primary_key=True)
    n_categoria = models.CharField(max_length=100, null=False)

class encargado_curso(models.Model):
    encargado_id= models.AutoField(primary_key=True)
    profesor =models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='username')

class curso(models.Model):
    curso_id= models.AutoField(primary_key=True)
    n_curso = models.CharField(max_length=100, null=False)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=False)
    fecha_termino = models.DateField(null=False)
    valor_curso = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descripcion = models.TextField(null=False)
    encargado = models.ForeignKey(encargado_curso, on_delete=models.CASCADE, db_column='profesor')

class Inscripcion(models.Model):
    inscripcion_id= models.AutoField(primary_key=True)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE, db_column='n_curso')
    usuario=models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='username')
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, null=False)

class contenido_curso(models.Model):
    contenido_id= models.AutoField(primary_key=True)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE, db_column='n_curso')
    titulo = models.CharField(max_length=100, null=False) 
    descripcion = models.TextField(null=False)

class pais(models.Model):
    pais_id= models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=100, null=False)

class Idioma(models.Model):
    idioma_id= models.AutoField(primary_key=True)
    nombre_idioma = models.CharField(max_length=100, null=False)

class clientes(models.Model):
    cliente_id= models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100, null=False)
    numero_domicilio = models.CharField(max_length=20, null=False)
    pais = models.ForeignKey(pais, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, null=False)
