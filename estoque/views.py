from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


class CatalogoList(ListView):  # template deve ter caracteristica de catalo
    model = Produto
    template_name = 'catalogo.html'


class CatalogoDetail(DetailView):
    model = Produto
    template_name = 'catalogo_detail.html'


class EstoqueList(ListView):  # deve ter aspecto de tabela e capacidade de filtro
    model = Produto
    template_name = 'controle_estoque.html'


class EstoqueCreate(CreateView):
    model = Produto
    template_name = 'estoque_create.html'
    fields = ['area_moveis', 'tipo', 'marca', 'nome', 'codigo_produto',
              'altura', 'largura', 'profundidade', 'preco', 'photo1',
              'photo2', 'photo3', 'disponiveis']
    success_url = '/estoque/controle_estoque'


class EstoqueUpdate(UpdateView):
    model = Produto
    fields = ['area_moveis', 'tipo', 'marca', 'nome', 'codigo_produto',
              'altura', 'largura', 'profundidade', 'preco', 'photo1',
              'photo2', 'photo3', 'disponiveis']
    template_name = 'estoque_update_form.html'
    success_url = '/estoque/controle_estoque'


class EstoqueDelete(DeleteView):
    model = Produto
    template_name = 'estoque_confirm_delete.html'
    success_url = reverse_lazy('controle')