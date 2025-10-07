from django.db import models
from django.contrib.auth.models import User

class Historico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    status = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.status}"
