from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')

        return render(request, 'login.html', {
            'error': 'El correo o la contraseña no son correctos.',
        }, status=401)

    return render(request, 'login.html')


@login_required(login_url='login')
def inicio(request):
    return render(request, 'inicio.html')


def pagina_no_encontrada(request, ruta_inexistente=None):
    return render(request, '404.html', status=404)