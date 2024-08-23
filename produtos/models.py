from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=5, decimal_places=2)