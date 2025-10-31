from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Plano(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    duracao_dias = models.IntegerField(help_text="Duração do plano em dias")

    def __str__(self):
        return self.nome


class Assinatura(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True, blank=True)
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(null=True, blank=True)

    def ativa(self):
       
        return self.data_fim and self.data_fim > timezone.now()

    def __str__(self):
        return f"{self.usuario.username} - {self.plano.nome if self.plano else 'Sem plano'}"


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)


    def __str__(self):
        return self.user.username





class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)


    def __str__(self):
        return self.user.username
    

    
