# Generated by Django 2.2.22 on 2021-06-03 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0010_auto_20210603_1424'),
        ('entregas', '0002_auto_20210602_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='venda',
        ),
        migrations.AddField(
            model_name='entrega',
            name='venda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vendas.Vendas'),
            preserve_default=False,
        ),
    ]
