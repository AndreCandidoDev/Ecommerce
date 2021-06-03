from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView
from home import urls as home_urls
from cliente import urls as cliente_urls
from estoque import urls as estoque_urls
from funcionarios import urls as funcionarios_urls
from vendas import urls as vendas_urls
from entregas import urls as entregas_urls

urlpatterns = [
    path('', include(home_urls)),
    path('cliente/', include(cliente_urls)),
    path('estoque/', include(estoque_urls)),
    path('funcionarios/', include(funcionarios_urls)),
    path('vendas/', include(vendas_urls)),
    path('entregas/', include(entregas_urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
