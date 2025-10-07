# historico/models.py
from django.db import models

class LinkHistorico(models.Model):
    url = models.URLField(unique=True)
    seguro = models.BooleanField(null=True)  #
    info = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
