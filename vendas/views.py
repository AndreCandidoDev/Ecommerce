from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Vendas
# Create your views here.

# client-size: verificar o produto que acabou de clicar em comprar e ao prencher form so com a qtd
# cria uma venda; cliente deve ter opção de visualizar suas compras e visualizar o status e ter opção de
# acompanhamento de entrega (deve estar logado para efetuar compra)


# admin-size: deve vizualizar as vendas e conferir os detalhes de cada uma.
# tambem deve ter opção de estaticas gerais (dashboard)

# client-size
class CompraCreate(CreateView):
    model = Vendas
    fields = ['quantidade', 'cpf', 'nome_completo', 'telefone', 'email']
    template_name = 'compra_new.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('compra_confirm')
    # apos confirmar compra deve levar o cliente para tela de opções de
    # pagamentos

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.produto_id = self.kwargs['produto_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dev_mode'] = True
        return context


def compra_confirm(request):
    return render(request, 'compra_confirm.html')


# admin size
class VendasList(ListView):
    model = Vendas
    template_name = 'vendas_list.html'


class VendasDetail(DetailView):
    model = Vendas
    template_name = 'vendas_detail.html'
