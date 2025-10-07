from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
