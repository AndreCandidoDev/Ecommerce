from django.db import models
from vendas.models import Vendas


class Entrega(models.Model):
    escolhas = (
        ('S', 'Sim'),
        ('N', 'Nao')
    )
    venda = models.ForeignKey(Vendas, on_delete=models.PROTECT)
    previsao = models.DateField()
    horario = models.TimeField(default='00:00')
    montagem = models.CharField(max_length=3, choices=escolhas, default='N')
    frete = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    endereco_completo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.previsao)
