"""
URL configuration for djangoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static  
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuario/", include("usuario.urls")),
    
    path("", TemplateView.as_view(template_name="home.html"), name="bemvindo"),
    path("login/", auth_views.LoginView.as_view(template_name="usuario/login.html"), name="login"),
    path("historico/", include("historico.urls")),
    path("plano/", include("plano.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('verificar/', views.verificar, name='verificar'),
    path('historico/', include('historico.urls')),
    path('admin/', admin.site.urls),
    path('historico/', include('historico.urls')),
    path("", include("historico.urls")),
    
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('usuario/', include('usuario.urls')),
    path('historico/', include('historico.urls')),
]
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
