from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .forms import UserForm, AdicionaisForm
from .models import *


class Gambiarra:
    def __init__(self):
        self.pega = None


def register_user(request):
    # form = UserCreationForm(request.POST or None, request.FILES or None)
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form)
        form.save()
        return redirect('adicionais')
    return render(request, 'cliente_form.html', {'form': form})


def register_adicionais(request):
    gamb = Gambiarra()
    gamb.pega = User.objects.all().last()
    print(gamb.pega)
    Adicionais(user=gamb.pega)
    print(Adicionais)
    print(Adicionais.objects.filter(user=gamb.pega))
    form = AdicionaisForm(request.POST or None)
    if form.is_valid():
        user = gamb.pega
        nome_completo = request.POST.get('nome_completo')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        celular = request.POST.get('celular')
        telefone_fixo = request.POST.get('telefone_fixo')
        lougradouro = request.POST.get('lougradouro')
        numero = request.POST.get('numero')
        cep = request.POST.get('cep')
        complemento = request.POST.get('complemento')
        adicional = request.POST.get('adicional')
        form = Adicionais(user=user, nome_completo=nome_completo, cpf=cpf, rg=rg, celular=celular, telefone_fixo=telefone_fixo,
                          lougradouro=lougradouro, numero=numero, cep=cep,
                          complemento=complemento, adicional=adicional)
        form.save()
        return redirect('home')
    return render(request, 'adicionais_form.html', {'form': form})


def cliente_list(request):
    if not request.user.is_superuser:
        return HttpResponse('Não autorizado')
    else:
        termo_busca = request.GET.get('pesquisa', None)
        if termo_busca:
            clientes = Adicionais.objects.all()
            clientes = clientes.filter(cpf=termo_busca)
            print(clientes)
        else:
            clientes = Adicionais.objects.all()  # recebe todos os elementos da tabela (model) Person
            print("Tabela adicionais", Adicionais.objects.all())
        return render(request, 'cliente_list.html', {'clientes': clientes})


def cliente_detail(request, id):  # rename to update
    if not request.user.is_superuser:
        return HttpResponse('Não autorizado')
    else:
        adicionais = get_object_or_404(Adicionais, pk=id)  # na tabela (model) Person procura (pk) a query id
        print(adicionais)
        form = AdicionaisForm(request.POST or None, request.FILES or None, instance=adicionais)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'cliente_detail.html', {'form': form})


def cliente_delete(request, id):
    cliente = get_object_or_404(Adicionais, pk=id)
    print(cliente)
    # form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        cliente.delete()
        return redirect('list')
    # return render(request, 'person_delete_confirm.html', {'form': form})
    return render(request, 'cliente_delete.html', {'cliente': cliente})