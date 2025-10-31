from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('verificar/', views.verificar_link, name='verificar_link'),
=======
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
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
]
