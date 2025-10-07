from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# historico/views.py
from django.shortcuts import render, redirect
from .models import LinkHistorico
import requests

def verificar_link(request):
    resultado = None
    info = ""
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            link_obj, created = LinkHistorico.objects.get_or_create(url=url)
            
            # Simples verificação de segurança
            try:
                response = requests.get(url, timeout=5)
                status_code = response.status_code
                link_obj.seguro = status_code == 200
                info = f"Status Code: {status_code}, Headers: {response.headers}"
            except Exception as e:
                link_obj.seguro = False
                info = str(e)
            
            link_obj.info = info
            link_obj.save()
            resultado = link_obj

    historico = LinkHistorico.objects.all().order_by('-criado_em')
    return render(request, "historico/historico.html", {
        "resultado": resultado,
        "historico": historico
    })


def verificar_url(request):
    return render(request, 'historico/verificar.html')


@login_required
def verificacao_view(request):
    return render(request, 'historico/verificacao.html')

@login_required
def historico_view(request):
    return render(request, 'historico/historico.html')
