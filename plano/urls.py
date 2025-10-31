from django.urls import path
from . import views

urlpatterns = [
    path("", views.planos_view, name="planos"),
    path("assinar/<int:plano_id>/", views.assinar_plano, name="assinar_plano"),
    path("pagamento/", views.pagamento_view, name="pagamento"),
    path("confirmar/<int:plano_id>/", views.confirmar_pagamento, name="confirmar_pagamento"),

]
