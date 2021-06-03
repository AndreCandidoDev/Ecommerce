from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Adicionais


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    # Nome = forms.CharField()
    last_name = forms.CharField()
    # Sobrenome = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        # fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class AdicionaisForm(ModelForm):
    class Meta:
        model = Adicionais
        fields = ('nome_completo', 'cpf', 'rg', 'celular', 'telefone_fixo', 'lougradouro',
                  'numero', 'cep', 'complemento', 'adicional')
#
#
# class DocumentosForm(ModelForm):
#     class Meta:
#         model = Documentos
#         fields = ('cpf', 'rg')
#
#
# class EnderecoForm(ModelForm):
#     class Meta:
#         model = Endereco
#         fields = ('lougradouro', 'numero', 'cep', 'complemento', 'adicional')
