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
    path('', include(enrutador.urls)),
    path('paises/lista_pais',views.paisListView.as_view(), name='lista_pais'),
    path('paises/crear_pais',views.paisCreateView.as_view(),name='crear_pais'),
    #path('Clientes/lista_usuario',views.usuarioCreateView.as_view(),name='lista_usuario')pass,
    #path('Clientes/crear_usuario',views.usuarioCreateView.as_view(),name='crear_usuario')pass,
    path('regiones/lista_region',views.regionesListView.as_view(),name='lista_region'),
    path('regiones/crear_region',views.regionesCreateView.as_view(),name='crear_region'),
    path('provincias/lista_provincia',views.provinciaListView.as_view(),name='lista_provincia'),
    path('provincias/crear_provincia',views.provinciaCreateView.as_view(),name='crear_provincia'),
]