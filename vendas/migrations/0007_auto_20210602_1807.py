# Generated by Django 2.2.22 on 2021-06-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0006_auto_20210602_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendas',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='vendas',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='vendas',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
