from django.urls import path, include
from .views import VendasList
from .views import VendasDetail
from .views import CompraCreate
from .views import compra_confirm

urlpatterns = [
    # path('compra_new/', CompraCreate.as_view(), name='compra_new'),
    path('compra_new/<int:produto_id>', CompraCreate.as_view(), name='compra_new'),
    path('compra_confirm/', compra_confirm, name='compra_confirm'),
    path('list_vendas/', VendasList.as_view(), name='list_vendas'),
    path('detail_vendas/<int:pk>/', VendasDetail.as_view(), name='detail_vendas'),
]