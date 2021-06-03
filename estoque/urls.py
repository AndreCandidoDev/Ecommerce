from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
# from .views import CatalogoList
# from .views import CatalogoDetail
from .views import EstoqueList
from .views import EstoqueCreate
from .views import EstoqueUpdate
from .views import EstoqueDelete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('catalogo/', CatalogoList.as_view(), name='catalogo'),
    # path('catalogo_detail/<int:pk>/', CatalogoDetail.as_view(), name='catalogo_detail'),
    path('estoque_create/', EstoqueCreate.as_view(), name='estoque_create'),
    path('estoque_update/<int:pk>/', EstoqueUpdate.as_view(), name='estoque_update'),
    path('estoque_delete/<int:pk>/', EstoqueDelete.as_view(), name='estoque_delete'),
    path('controle_estoque/', EstoqueList.as_view(), name='controle'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()