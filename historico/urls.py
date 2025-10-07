from django.urls import path
from . import views
from .views import verificar_link


def verificacao_view(request):
    urlpatterns = [
    path("historico/", verificar_link, name="historico"),
]



    urlpatterns = [
    path('verificar/', views.verificar_view, name='verificar'),
]


urlpatterns = [
    path('', views.verificacao_view, name='verificacao'),
    path('historico/', views.historico_view, name='historico'),
]
