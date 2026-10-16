# Proyecto de Cursos API REST con Django

Se entregará la explicacion del procedimiento realizado dentro de este proyecto, la cual tiene por finalidad crear un sistema de cursor, contando con la posibilidad de implementar vistas, conexión con base de datos y generar los procedimientos CRUD(Create-Read-Update-Detele)


## 1. Crear ambiente virtual

El primer procedimiento a realizar es generar un ambiente vistual el que nos permitirá trabajar de una forma segura en nuestro proyecto, esta debe encontrarse en la carpeta raíz:

```bash
python -m venv {nombre_ambiente}
```

`venv` significa Virtual Environment (entorno virtual), y sirve para aislar dependencias del proyecto sin afectar la instalación global de Python.

## 2. Activar el ambiente virtual

Encontrandonos en la carpeta raizm, es necesario dirigirnos a esta ruta, la cual permitira iniciar nuestro ambiente virtual:

```powershell
.\{nombre_ambiente}\Scripts\Activate.ps1
```

Si este se bloquea por seguridad, se debe ejecutar:

```powershell
Set-ExecutionPolicy Bypass -Scope CurrentUser
```

Luego vuelve a activar el entorno.


## 3. Actualizar pip
Dentro de las buenas practicas, se encuentra la revisión y ejecución de los scripts que puedan solicitar actualización, lo que permitira rendir dentro del proceso sin la posibilidad de incompatibilidades:

```bash
python -m pip install --upgrade pip
```

## 4. Instalar dependencias (Solo en caso de tener tu archivo requirements.txt)

Dentro del entorno virtual, instala las librerías del proyecto:

```bash
pip install -r requirements.txt
```
## 5. Instalación de entorno Django
Una vez ubicados en la terminal de trabajo, es necesaria la instalación de la siguiente dependencia desde la carpeta raíz:

```bash
pip install django
```
una vez se ejecute comando, se instalaran las siguientes depedencias, las cuales serán necesarias en un futuro:
- 'asgiref'
- 'django'
- 'sqlparse'
- 'tzdata'
## 6. Instalación entorno Django
El siguiente comando entregará los recursos necesarios para django y su correcta funcionalidad al momento de ejecutar nuestro backend:

```bash
django-admin startproject {nombre_motor} .
```
Esto crea la estructura requerida para la configuracion de los siguientes elementos:
- 'settings.py' : Configuraciónes generales del sistema
- 'urls.py' :creacion de rutas para los request de la aplicación

## 7. Crear Aplicación
Luego de crear el archivo motor de nuestro sistema, se deberá crear la carpeta con todas las dependencias necesarias para la ejecución de nuestra aplicación:

```bash
django-admin startapp {nombre_app} .
```

En este directorio se encontraran los siguientes archivos:
- 'admin.py' : Permitira crear el CRUD del modelo de datos, por lo que necesitaremos registrar los modelos implementados.
- 'app.py' : Define configuraciónes especificas
- 'models.py' : Acá se definirán los modelos los cuales se trabajaran en la applicación.
- 'test.ppy' : Definición de trabajos de testing de forma unitaria.
- 'views.py' : Controlador logico de solicitudes(REQUEST) que seran enviadas como respuesta(RESPONSE), respondiendo al modelo logico basado en funciones.

Cuando ya este todo listo, en nuestra consola de comandos ejecutaremos el siguiente comando:

```bash
python manage.py runserver
```
## 7.1 Configuración en *settings.py*

Cuando arraque nuestro servidor, entregara una pagina por defecto originada por Djang, pero esto no debe quedar asi, puesto que nosotros debemos implementar nuestras vistas, por lo que sera necesario agregar en settings lo siguiente:

```bash
INSTALLED_APPS = [
    # apps de django
    'mi_aplicacion',
]
```
Esto permitira el reconocimiento de todo lo que se encuentre dentro de nuestra aplicación.
Para que se logren ver las views que nosotros vayamos implementando es necesario realizar el siguiente cambio en el mismo apartado:

```bash
DEBUG = FALSE
```
```bash
ALLOWED_HOSTS = ["127.0.0.1","localhost"]
```
- 'Debug' : quitará la edición en formato de prueba.
- 'ALLOWED_HOSTS' : reconocera el procedimiento de trabajo en host_local.

*Esto adelantará el proceso de seguridad y autorización de servidor local*

y para finalizar, tendremos que crear un directorio que permita referenciar los archivos .html, determinando un orden logico de las vistas para luego establecer de que forma se comunicará el llamado a estas. para eso, será necesario:

-------------------------
------------------------- Views -------------------------
```bash
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html') .
```

------------------------- 
------------------------- urls -------------------------

```bash
from {mi_aplicacion} import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
] .
```
-------------------------
## 8. Modelo de datos
Aqui trabajaremos en el archivo *models.py*, en el cual debemos crear nuestro modelo de datos, el cual deberá cumplir con la siguiente estructura:
```bash
from django.db import models

class MiClase(models.Model):
    atributo_1 = models.CharField('Campo 1',max_length=25,null=false)
    atributo_2 = models.TextField('Campo 2',max_length=100,null=false)
    atributo_3 = models.DateField('Campo 3',null=false)
    atributo_4 = models.TimeField('Campo 4',null=false)
    atributo_5 = models.DateTimeField('Campo 5',max_length=100,null=false)
    atributo_6 = models.IntegerField('Campo 6',)

class MiClase2(models.Model):
    atributo_referenciado = models.ForeignKey(MiClase,on_delete=CASCADE)
    atributo_2 = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
```
una vez ya esten creadas estas, procederemos a utilizar los siguientes comandos:

```bash
python manage.py makemigrations
```
- Registra los cambios realizados o generados en la base de datos
```bash
python manage.py migrate
```
- Genera los cambios tanto en la carpeta migrations como en la base de datos a utilizar.

## 9. Manejo de Base de datos
En el siguiente paso sera requerido el lograr manejar nuestra base de datos desde un ambiente especifico, como tambien desde un usuario especifico, para ello una vez ubicado en nuestro motor, se deberá ejecutar las siguientes lineas de codigo:

### Remoto
```bash
CREATE USER 'Usuario'@'%' IDENTIFIED BY 'mi_contraseña';
```
```bash
GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'Usuario'@'%';
```
```bash
FLUSH PRIVILEGES;
``` 
### Local
```bash
CREATE USER 'Usuario'@'localhost' IDENTIFIED BY 'mi_contraseña';
```
```bash
GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'Usuario'@'localhost';
```
```bash
FLUSH PRIVILEGES;
```
Para otorgar la comunicacion hacia el ambiente de base de datos, será necesaria la instalación del siguiente script

```bash
pip install SQLAlchemy mysqlclient
```
## 10. Datos iniciales de la aplicación

Para portar los datos que necesitemos a nuestra base de datos, es requerido adaptar el modelo de datos a los cuales nos vamos a referir de la siguiente manera:

```bash
[
    {
        "model": "mi_aplicacion.nombre_modelo",
        "pk": 1,
        "fields": {
            "atributo_1": "01",
            "atributo_2": "Atributo 2"
        }
    },
    {
        "model": "mi_aplicacion.nombre_modelo",
        "pk": 2,
        "fields": {
            "atributo_1": "02",
            "atributo_2": "Atributo 2"
        }
    }
]
```
- 'pk': es el codigo generado de forma automatica
- 'model': entregará la referencia al modelo utilizado

## 11. Desacoplar Datos sensibles
Puesto que ya nos encontramos trabajando con una base de datos externa, es necesario determinar las credenciales a utilizar en esta base de datos, para eso, debemos extraer las contraseñas como datos sensibles del codigo, para eso sera necesaria la instalacion de la siguiente librería:
```bash
pip install python-decouple
```
- A continuacion tambien sera necesario crear un archivo *.env*, el cual almacenará los datos sensibles y debera ubicarce en la carpeta raiz.
```bash
SECRET_KEY='cadena_de_caracteres_django_secret_key'
```
Luego para utilizar este dato, se deberá ingresar en settings.py en conjunto a la librerí de la sigueinte manera:

```bash
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```
## 12. Django Rest Framework

Rest Framework es una librería con muchas herramientas las cuales permitiran seguir el desarrollo de serializadores.
para esto sera necesario instalar esta de la siguiente manera desde nuestra terminal:

```bash
pip install djangorestframework
```

Luego de haber instalado este, hay que agregarlo al listado de INSTALLED_APPS en *settings.py* de la siguiente manera:

```bash
INSTALLED_APPS = [ ... 'rest_framework', ... ]
```
## 13. Incorporación de modelo de datos al administrador de Django

En nuetras carpeta admin.py se deben registrar cada uno de los modelos de datos incorporados en nuestro sistema, esto permitira que el administrador de django realice el proceso de los datos a utilizar, y se requerira de la siguiente manera:
```bash
from django.contrib import admin
from .models import {clases}

admin.site.register({clase1})
admin.site.register({clase2})
admin.site.register({clase3})
```
## 14. Serializadores
Con la misma librería anteriormente instalada, permitira el manejo de los datos con el modelo de datos implementados desde el formato .JSON, el cual permitira trabajar desde la aplicación web. para implementar de forma correcta hay que seguir el siguiente procedimeinto:

 1. Crear Archivo *serializer.py*: este debe encontrarse en la carpeta raiz de nuestra aplicación(aplicación_app).
 2. Importar los serializadores de nuestros modelos. 
 3. Importar todos los modelos de models.py
 4. Crear una clase encargada de serializar el modelo de datos.

```bash
from .models import MiClase
from .models import MiClase2

class MiClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiClase
        fields = ('__all__')
        # __all__ serializa todas los atributos de la clase/modelo

class MiClase2Serializer(serializers.ModelSerializer):
    class Meta:
        model = MiClase2
        fields = ('atributo_referenciado','atributo_2')
        # De esta forma nosotros decidimos qué atributos de nuestra clase/modelo se serializarán
``` 
## 15. Vistas Basadas en Clases

Este nos permitira visualizar nuestro modelo de datos y a su vez realizar el CRUD a los datos en estos. Para crear este es necesario implementarlo a nuestro views.py de la siguiente manera:

```bash
from rest_framework import viewsets 
from .models import Miclase, Miclase2
from .serializer import MiClaseSerializer, MiClase2Serializer
```

``` bash
class MiClaseViewSet(viewsets.ModelViewSet):
    queryset = MiClase.objects.all()
    serializer_class = MiClaseSerializer

class MiClase2ViewSet(viewsets.ModelViewSet):
    queryset = MiClase2.objects.all()
    serializer_class = MiClase2Serializer
```

## 16. Creación de Rutas

Para lograr tener las vistas otorgadas directamente desde la libreria de Django y generar el proceso de crud, es necesario determinar los End-Points, para ello tendremos que definir las rutas a utilizar:
- En el directorio de nuestra aplicacion (Aplicación_app) tendremos que crear un nuevo archivo *urls.py* en el cual se gestionaran las ruitas de los modelos.
- En estos generaremos los siguientes objetos:
>routers.DefaultRouter
- Se deberan registrar los siguientes metodos para dejar disponibles los objetos, para ello utilizaremos un ViewSet de la siguiente forma:
```bash
from django.urls import path,include
from rest_framework import routers
from mi_aplicacion import views

enrutador = routers.DefaultRouter()

enrutador.register(r'miclase', views.MiClaseViewSet)
enrutador.register(r'miclase2', views.MiClase2ViewSet)

urlpatterns = [
    path('', include(enrutador.urls))
]
```

- 'r': genera la ruta y evita los saltos de linea
- 'urlpatterns': incluye las rutas dentro del enrutador

## 17. Incorporación de rutas a django
 Para las rutas generadas y estas queden disponibles, se deberá incorporar de la siguiente manera:
```bash
from django.contrib import admin
from django.urls import path,include
from mi_aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),
    path('mi_aplicacion/', include('mi_aplicacion.urls')),
]
```
--------------------------------------------------------
Se recomienda mantener la configuración sensible fuera del código fuente. El proyecto usa `python-decouple` y espera un archivo `.env` en la raíz del proyecto.

Crea un archivo `.env` con este contenido:
```env
SECRET_KEY=tu_secret_key_aqui
USER=tu_usuario_mysql
USER_KEY=tu_password_mysql
```

> Importante: no subir credenciales reales al repositorio público.
--------------------------------------------------------
## 18. Endpoints principales de la API

El proyecto incluye rutas REST con router, por ejemplo:

- `http://127.0.0.1:8000/api/cursos/`
- `http://127.0.0.1:8000/api/categoria/`
- `http://127.0.0.1:8000/api/Inscripcion/`
- `http://127.0.0.1:8000/api/contenido_curso/`
- `http://127.0.0.1:8000/api/pais/`
- `http://127.0.0.1:8000/api/Idioma/`
- `http://127.0.0.1:8000/api/region/`
- `http://127.0.0.1:8000/api/clientes/`
- `http://127.0.0.1:8000/api/provincia/`
- `http://127.0.0.1:8000/api/encargado_curso/`


Estos endpoints permiten realizar operaciones CRUD usando los verbos HTTP:
- GET: listar o consultar
- POST: crear
- PUT: actualizar completo
- PATCH: actualización parcial
- DELETE: eliminar
