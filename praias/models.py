from django.db import models

# Create your models here.
class Relatorios(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False, unique=True)
    url = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.url


class Praias(models.Model):
    nome = models.CharField(max_length=150)
    descr = models.CharField(max_length=250)
    ref = models.CharField(max_length=10, unique=True, blank=False, null=False)
    bairro = models.CharField(max_length=150, null=False, blank=False)
    coord = models.CharField(max_length=50, unique=True)
    mapa = models.CharField(max_length=500)
    propria = models.BooleanField(default=False)
    atualizado_em = models.DateTimeField()

    def __str__(self):
        return self.nome