from django.urls import path
from django.http import HttpResponse


def plano_list(request):
    return HttpResponse("Página de planos funcionando!")


def placeholder_view(request):
    return HttpResponse("Página de planos funcionando!")

urlpatterns = [
    path('', placeholder_view, name='plano_home'),
]
