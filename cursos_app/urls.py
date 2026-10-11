from django.urls import path,include
from rest_framework import routers
from cursos_app import views

enrutador = routers.DefaultRouter()

enrutador.register(r'cursos', views.cursoViewSet)
enrutador.register(r'encargado_curso', views.encargado_cursoViewSet)
enrutador.register(r'categoria', views.categoriaViewSet)
enrutador.register(r'Inscripcion', views.InscripcionViewSet)
enrutador.register(r'contenido_curso', views.contenido_cursoViewSet)
enrutador.register(r'pais', views.paisViewSet)
enrutador.register(r'Idioma', views.IdiomaViewSet)
enrutador.register(r'region', views.regionViewSet)
enrutador.register(r'clientes', views.clientesViewSet)
enrutador.register(r'provincia', views.provinciaViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),]