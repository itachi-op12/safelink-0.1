from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.planos_view, name="planos"),
    path("assinar/<int:plano_id>/", views.assinar_plano, name="assinar_plano"),
    path("pagamento/", views.pagamento_view, name="pagamento"),
    path("confirmar/<int:plano_id>/", views.confirmar_pagamento, name="confirmar_pagamento"),

=======
  
    path('', views.plano_list, name='plano_list'),
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
]
