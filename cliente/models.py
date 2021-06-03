from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# procurar o model padrao de usuario e atribuir como chave primaria a classe dados


class Adicionais(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=8, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    telefone_fixo = models.CharField(max_length=11, null=True, blank=True)
    lougradouro = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=6, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    adicional = models.TextField(null=True, blank=True)

    @property
    def usuario(self):
        return self.user

    def __str__(self):
        return str(self.user)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Adicionais.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.adicionais.save()


# class Documentos(models.Model):
#     cpf = models.CharField(max_length=14)
#     rg = models.CharField(max_length=8)
#
#
# class Endereco(models.Model):
#     lougradouro = models.CharField(max_length=100)
#     numero = models.IntegerField()
#     cep = models.CharField(max_length=9)
#     complemento = models.CharField(max_length=100)
#     adicional = models.TextField(null=True, blank=True)
#
#
# class Dados(models.Model):
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#     documentos = models.OneToOneField(Documentos, on_delete=models.CASCADE)
#     endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)