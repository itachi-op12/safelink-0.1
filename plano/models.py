from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    limite_verificacoes = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.nome} - R${self.preco}"
