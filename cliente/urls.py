from django.contrib import admin
from django.urls import path
from .views import register_user
from .views import register_adicionais
from .views import cliente_list
from .views import cliente_detail
from .views import cliente_delete
# from .views import cliente_update

urlpatterns = [
    path('register/', register_user, name='register'),
    path('adicionais/', register_adicionais, name='adicionais'),
    path('cliente_list/', cliente_list, name='list'),
    path('cliente_detail/<int:id>', cliente_detail, name='detail'),
    path('delete/<int:id>/', cliente_delete, name='delete'),
    # path('cliente_update/<int:id>/', cliente_update, name='detail'),
]