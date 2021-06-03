from django.db import models


class Produto(models.Model):
    Area_moveis = (
        ('Quarto', 'Quarto'),
        ('Cozinha', 'Cozinha'),
        ('Escritorio', 'Escritorio'),
        ('Sala', 'Sala'),
        ('Area-de-servico', 'Area-de-servico'),
        ('Externo', 'Externo'),
        ('Usados', 'Usados'),
        ('Outro', 'Outro')
    )
    Tipo_moveis = (
        ('Guarda-roupa', 'Guarda-roupa'),
        ('Armario', 'Armario'),
        ('Mesa', 'Mesa'),
        ('Cadeira', 'Cadeira'),
        ('Rack', 'Rack'),
        ('Painel', 'Painel'),
        ('Cristaleira', 'Cristaleira'),
        ('Estante', 'Estante'),
        ('Fruteira', 'Fruteira'),
        ('Sapateira', 'Sapateira'),
        ('Balcão', 'Balcão'),
        ('Paneleiro', 'Paneleiro'),
        ('Cama', 'Cama'),
        ('Outro', 'Outro'),
    )
    area_moveis = models.CharField(max_length=60, choices=Area_moveis, default='Sem-area')
    tipo = models.CharField(max_length=60, choices=Tipo_moveis, default='Sem-tipo')
    marca = models.CharField(max_length=60)
    nome = models.CharField(max_length=100)
    codigo_produto = models.CharField(max_length=100, null=True, blank=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    largura = models.DecimalField(max_digits=3, decimal_places=2)
    profundidade = models.DecimalField(max_digits=3, decimal_places=2)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    photo1 = models.ImageField(upload_to='products_photos/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='products_photos/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='products_photos/', null=True, blank=True)
    disponiveis = models.IntegerField(default=0)

    def __str__(self):
        return str(self.nome)

