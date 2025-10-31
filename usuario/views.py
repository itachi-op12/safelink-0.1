from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, PerfilForm
from .models import Perfil
from historico.models import Historico
from .models import PerfilUsuario 
from plano.models import PlanoAtivo
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Plano, Assinatura
from .forms import AssinaturaForm
from django.shortcuts import redirect
from django.contrib.auth import logout


def verificar_email(request):
    return render(request, 'usuario/verificar_email.html')

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verificar_link')
    
    else:
        form = RegistroForm()
    return render(request, "usuario/cadastro.html", {"form": form})

@login_required
def perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'usuario/perfil.html', {'form': form, 'perfil': perfil})

def sair(request):
    logout(request)
    return redirect('login')



@login_required
def planos(request):
    planos = Plano.objects.all()
    return render(request, "usuario/planos.html", {"planos": planos})


@login_required
def assinar_plano(request, plano_id):
    plano = get_object_or_404(Plano, id=plano_id)

   
    data_inicio = timezone.now()
    data_fim = data_inicio + timedelta(days=plano.duracao_dias)

    assinatura, criada = Assinatura.objects.update_or_create(
        usuario=request.user,
        defaults={
            "plano": plano,
            "data_inicio": data_inicio,
            "data_fim": data_fim
        }
    )

    return redirect("perfil")


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_login(request, form.get_user())
        return redirect('login') 
    


from django.shortcuts import render, redirect
from .forms import PerfilForm

def perfil_view(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil.html', {'form': form, 'perfil': perfil})



def logout_view(request):
    logout(request)
    return redirect('login')  # redireciona para a tela de login depois de sair


=======
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('verificacao')  
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'usuario/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Esse nome de usuário já está em uso!')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('verificacao')  
    return render(request, 'usuario/cadastro.html')
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
