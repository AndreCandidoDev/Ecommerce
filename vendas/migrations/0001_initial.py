# Generated by Django 2.2.22 on 2021-05-31 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estoque', '0004_auto_20210529_1247'),
        ('cliente', '0003_auto_20210528_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('impostos', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('AB', 'Aberta'), ('FC', 'Fechada'), ('PC', 'Processando'), ('DC', 'Desconhecido')], default='DC', max_length=2)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cliente.Adicionais')),
            ],
            options={
                'verbose_name_plural': 'Vendas',
                'permissions': (('setar_nfe', 'Usuario pode alterar parametro NF-e'), ('ver_dashboard', 'Pode visualizar o Dashboard'), ('permissao3', 'Permissao 3')),
            },
        ),
        migrations.CreateModel(
            name='ItemDoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Vendas')),
            ],
            options={
                'verbose_name_plural': 'Itens do pedido',
                'unique_together': {('venda', 'produto')},
            },
        ),
    ]