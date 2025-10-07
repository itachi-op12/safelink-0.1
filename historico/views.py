from django.shortcuts import render
#from django.contrib.auth.decorators import login_required


def verificacao(request):
    return render(request, 'historico/verificacao.html')
