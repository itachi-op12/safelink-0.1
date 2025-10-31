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
