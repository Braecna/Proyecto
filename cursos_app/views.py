from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render

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