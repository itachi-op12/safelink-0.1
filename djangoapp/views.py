

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  

def verificar(request):
    return render(request, 'verificar.html')  
