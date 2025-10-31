<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Plano, PlanoAtivo
from .models import Plano
from django.shortcuts import render

def planos_view(request):
    planos = [
        {"nome": "Semanal", "preco": "R$3,99", "descricao": "Acesso completo por 7 dias."},
        {"nome": "Mensal", "preco": "R$9,99", "descricao": "Ideal para uso contínuo."},
        {"nome": "Anual", "preco": "R$39,99", "descricao": "Economize 40% com o plano anual."},
    ]
    return render(request, "plano/plano.html", {"planos": planos})

def pagamento_view(request):
    plano_nome = request.GET.get('plano')
    plano = get_object_or_404(Plano, nome=plano_nome)
    return render(request, 'plano/pagamento.html', {'plano': plano})


@login_required
def assinar_plano(request, plano_id):
    plano = get_object_or_404(Plano, id=plano_id)
    PlanoAtivo.objects.update_or_create(usuario=request.user, defaults={"plano": plano})
    return redirect("planos")

@login_required
def confirmar_pagamento(request, plano_id):
    plano = get_object_or_404(Plano, id=plano_id)
    return render(request, "plano/confirma_pagamento.html", {"plano": plano})

=======
from django.urls import path
from django.http import HttpResponse


def plano_list(request):
    return HttpResponse("Página de planos funcionando!")


def placeholder_view(request):
    return HttpResponse("Página de planos funcionando!")

urlpatterns = [
    path('', placeholder_view, name='plano_home'),
]
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
