from django.db import models
from django.db.models import Sum, F, FloatField, Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from .managers import VendaManager
from cliente.models import Adicionais
from estoque.models import Produto

# botao comprar deve criar uma nova venda, o da main page redireciona ao um formulario onde o usuario
# deve passar a quantidade desejada e ao acionar o botao confirmar compra criando a venda e o redirecionando
# para formulario de entrega


class Vendas(models.Model):
    ABERTA = 'AB'
    FECHADA = 'FC'
    PROCESSANDO = 'PC'
    DESCONHECIDO = 'DC'
    STATUS = (
        (ABERTA, 'Aberta'),
        (FECHADA, 'Fechada'),
        (PROCESSANDO, 'Processando'),
        (DESCONHECIDO, 'Desconhecido')
    )
    numero = models.CharField(max_length=7, null=True, blank=True)  # deve ser sequencial iniciando em 1
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # impostos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantidade = models.FloatField()
    cpf = models.CharField(max_length=14, null=True, blank=True)
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    # pessoa = models.ForeignKey(Adicionais, null=True, blank=True, on_delete=models.PROTECT)
    status = models.CharField(choices=STATUS, default=DESCONHECIDO, max_length=2, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, null=True, blank=True)

    # objects = VendaManager()
    def get_absolute_url(self):
        return reverse('home', args=[self.produto.id])

    class Meta:
        verbose_name_plural = "Vendas"

    # def calcular_total(self):
    #     tot = self.vendas_set.all().aggregate(
    #         # tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
    #         tot_ped=Sum((F('quantidade') * F('produto__preco')), output_field=FloatField())
    #     )['tot_ped'] or 0
    #     # tot = tot - float(self.impostos) - float(self.desconto)
    #     self.valor = tot
    #     self.save()
        # Vendas.objects.filter(id=self.id).update(valor=tot)

    def __str__(self):
        return self.nome_completo if self.cpf else 'no data'


# @receiver(post_save, sender=ItemDoPedido)
# def update_vendas_total(sender, instance, **kwargs):
#     instance.venda.calcular_total()
#
#
# @receiver(post_save, sender=Vendas)
# def update_vendas_total2(sender, instance, **kwargs):
#     instance.calcular_total()
