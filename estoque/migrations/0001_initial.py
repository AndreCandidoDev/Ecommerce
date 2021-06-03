# Generated by Django 2.2.22 on 2021-05-26 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_movel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_do_movel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('codigo_produto', models.CharField(blank=True, max_length=100, null=True)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('largura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('profundidade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='products_photos')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='products_photos')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='products_photos')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Categoria')),
            ],
        ),
    ]