# historico/models.py
from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
class Historico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    status = models.CharField(max_length=20)  # "Seguro", "Perigoso", etc.
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.url}"
=======
class LinkHistorico(models.Model):
    url = models.URLField(unique=True)
    seguro = models.BooleanField(null=True)  #
    info = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
