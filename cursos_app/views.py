from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render
from .models import curso, encargado_curso, categoria, Inscripcion, contenido_curso, pais, Idioma, clientes, provincia, region
from .serializer import cursoSerializer, encargado_cursoSerializer, categoriaSerializer, InscripcionSerializer, contenido_cursoSerializer, paisSerializer, IdiomaSerializer, clientesSerializer, provinciaSerializer, regionSerializer
from rest_framework import viewsets
from django.views.generic import ListView
# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        user_model = get_user_model()
        try:
            account = user_model._default_manager.get(email__iexact=email)
            username = account.get_username()
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            username = email

        user = authenticate(
            request,
            **{user_model.USERNAME_FIELD: username, 'password': password},
        )

        if user is not None:
            login(request, user)
            return redirect('inicio')

        return render(request, 'login.html', {
            'error': 'El correo o la contraseña no son correctos.',
        }, status=401)

    return render(request, 'login.html')

def inicio(request):
    return render(request, 'inicio.html')


def pagina_no_encontrada(request, ruta_inexistente=None):
    return render(request, '404.html', status=404)



#vistas basadas en clase
class cursoViewSet(viewsets.ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer
class encargado_cursoViewSet(viewsets.ModelViewSet):
    queryset = encargado_curso.objects.all()
    serializer_class = encargado_cursoSerializer
class categoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer
class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
class contenido_cursoViewSet(viewsets.ModelViewSet):
    queryset = contenido_curso.objects.all()
    serializer_class = contenido_cursoSerializer

class paisViewSet(viewsets.ModelViewSet):
    queryset = pais.objects.all()
    serializer_class = paisSerializer
class paisListView(ListView):
    model = pais
    template_name = 'cursos_app/templates/cursos_app/paises/pais_list.html'
    
class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
class clientesViewSet(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = clientesSerializer
class provinciaViewSet(viewsets.ModelViewSet):
    queryset = provincia.objects.all()
    serializer_class = provinciaSerializer
class regionViewSet(viewsets.ModelViewSet):
    queryset = region.objects.all()
    serializer_class = regionSerializer


