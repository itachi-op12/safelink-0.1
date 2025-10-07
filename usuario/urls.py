from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # raiz do app
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
]
