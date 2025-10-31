from django.db import models
from django.contrib.auth.models import User

class Historico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    status = models.CharField(max_length=20)  # "Seguro", "Perigoso", etc.
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.url}"
