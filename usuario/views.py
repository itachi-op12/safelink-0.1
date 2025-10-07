from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
""


def home(request):
    return render(request, 'home.html')


def perfil(request):
    return render(request, 'perfil.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('verificacao')
    return render(request, 'usuario/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Preencha todos os campos!')
            return render(request, 'usuario/cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Esse nome de usuário já está em uso!')
            return render(request, 'usuario/cadastro.html')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login')  # redireciona para login

    # CASO GET: sempre retorna a página de cadastro
    return render(request, 'usuario/cadastro.html')