from django.contrib import admin
from django.urls import path
from .views import CatalogoList, CatalogoDetail,Logout, contato
from .views import termos, privacidade, dados

urlpatterns = [
    path('', CatalogoList.as_view(), name='home'),
    path('detail/<int:pk>', CatalogoDetail.as_view(), name='catalogo_detail'),
    path('logout/', Logout, name='logout'),
    path('contato/', contato, name='contato'),
    path('termos_de_uso/', termos, name='termos'),
    path('privacidade/', privacidade, name='privacidade'),
    path('dados/', dados, name='dados'),
]