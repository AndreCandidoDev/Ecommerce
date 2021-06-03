from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'funcionarios_list.html'


class FuncionarioDetail(DetailView):
    model = Funcionario
    template_name = 'funcionarios_detail.html'


class FuncionarioCreate(CreateView):
    model = Funcionario
    template_name = 'funcionarios_create.html'
    fields = ['cpf', 'rg', 'image_cpf', 'image_rg', 'nome_completo',
              'telefone', 'pis_pasep', 'numero_serie_ctps', 'data_admissao',
              'funcao', 'jornada_de_trabalho', 'status', 'horas_trabalhadas',
              'horas_extras', 'dia_pagamento']
    success_url = '/funcionarios/funcionarios_list'


class FuncionarioUpdate(UpdateView):
    model = Funcionario
    template_name = 'funcionarios_update_form.html'
    fields = ['cpf', 'rg', 'image_cpf', 'image_rg', 'nome_completo',
              'telefone', 'pis_pasep', 'numero_serie_ctps', 'data_admissao',
              'funcao', 'jornada_de_trabalho', 'status', 'horas_trabalhadas',
              'horas_extras', 'dia_pagamento']
    success_url = '/funcionarios/funcionarios_list'


class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'funcionarios_confirm_delete.html'
    success_url = reverse_lazy('funcionarios_list')