from django.db import models


class Funcionario(models.Model):
    Status = (
        ('Ativo', 'ativo'),
        ('Licenciado', 'licenciado'),
        ('Ferias', 'ferias'),
        ('Desligado', 'desligado'),
    )
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    image_cpf = models.ImageField(upload_to='documents/', blank=True, null=True)
    image_rg = models.ImageField(upload_to='documents/', blank=True, null=True)
    nome_completo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    pis_pasep = models.CharField(max_length=100)
    numero_serie_ctps = models.CharField(max_length=100)
    data_admissao = models.DateField()
    funcao = models.CharField(max_length=100)
    jornada_de_trabalho = models.IntegerField()
    status = models.CharField(max_length=100, choices=Status)
    horas_trabalhadas = models.DecimalField(max_digits=10, decimal_places=2)
    horas_extras = models.DecimalField(max_digits=10, decimal_places=2)
    dia_pagamento = models.CharField(max_length=100, default='10')

    def __str__(self):
        return str(self.nome_completo)
