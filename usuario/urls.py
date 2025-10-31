from django.urls import path
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="usuario/login.html"), name="login"),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logout_view, name='logout'),
    path('planos/', views.planos, name='planos'),
    path('sair/', views.sair, name='sair'),
    path("assinar/<int:plano_id>/", views.assinar_plano, name="assinar_plano"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("verificar-email/", views.verificar_email, name="verificar_email"),

   
=======
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
]
