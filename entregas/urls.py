from django.contrib import admin
from django.urls import path, include
from .views import ListEntregas
from .views import CreateEntrega

urlpatterns = [
    path('list_entregas/', ListEntregas.as_view(), name='list_entregas'),
    path('create_entregas/', CreateEntrega.as_view(), name='create_entregas'),
]