from django.db import models
from django.contrib.auth.models import User

class Plano(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    duracao = models.CharField(max_length=20)  
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.duracao})"

class PlanoAtivo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    data_assinatura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.plano.nome}"
