<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Historico
from .forms import VerificarLinkForm
import re

@login_required
def verificar_link(request):
    resultado = None
    if request.method == "POST":
        form = VerificarLinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]

            # --- Lógica simples de segurança ---
            if not re.match(r'^https?://', url):
                status = "Inválido"
            elif any(suspeito in url for suspeito in [".ru", ".xyz", "bit.ly", "shorturl", "tinyurl"]):
                status = "Suspeito"
            elif url.startswith("https://"):
                status = "Seguro"
            else:
                status = "Desconhecido"

            Historico.objects.create(usuario=request.user, url=url, status=status)
            resultado = {"url": url, "status": status}
    else:
        form = VerificarLinkForm()

    historicos = Historico.objects.filter(usuario=request.user).order_by("-data")[:10]
    return render(request, "historico/verificar.html", {
        "form": form,
        "resultado": resultado,
        "historicos": historicos
    })
=======
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
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
