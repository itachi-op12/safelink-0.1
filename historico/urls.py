from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_link, name='verificar_link'),
]
