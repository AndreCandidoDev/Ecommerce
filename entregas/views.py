from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Entrega


class ListEntregas(ListView):
    model = Entrega
    template_name = 'entregas_list.html'


class CreateEntrega(CreateView):
    model = Entrega
    fields = ['venda', 'previsao', 'horario', 'montagem',
              'frete']
    template_name = 'entregas_create.html'
    success_url = '/entregas/list_entregas'
