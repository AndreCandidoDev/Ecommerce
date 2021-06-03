# Generated by Django 2.2.22 on 2021-05-23 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adicionais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('rg', models.CharField(blank=True, max_length=8, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('telefone_fixo', models.CharField(blank=True, max_length=11, null=True)),
                ('lougradouro', models.CharField(blank=True, max_length=100, null=True)),
                ('numero', models.CharField(blank=True, max_length=6, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('adicional', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]