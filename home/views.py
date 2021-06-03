from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from estoque.models import Produto


class CatalogoList(ListView):  # template deve ter caracteristica de catalo
    model = Produto
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dev_mode'] = True
        return context


class CatalogoDetail(DetailView):
    model = Produto
    template_name = 'catalogo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dev_mode'] = True
        return context


# def home(request): # refatorar para exibir o catalogo
#     return render(request, 'home.html')


def termos(request):
    return render(request, 'termos_de_servico.html')


def privacidade(request):
    return render(request, 'politica_de_privacidade.html')


def dados(request):
    return render(request, 'exclusao_de_dados.html')


def Logout(request):
    logout(request)
    return redirect('home')


def contato(request):
    return render(request, 'contato.html')