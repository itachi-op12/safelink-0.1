from django.contrib import admin
from .models import Plano, PlanoAtivo

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ("nome", "duracao", "preco")
    search_fields = ("nome", "duracao")

@admin.register(PlanoAtivo)
class PlanoAtivoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "plano", "data_assinatura")
    list_filter = ("plano",)
