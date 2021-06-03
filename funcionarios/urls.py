from django.urls import path
from .views import FuncionarioList
from .views import FuncionarioDetail
from .views import FuncionarioCreate
from .views import FuncionarioUpdate
from .views import FuncionarioDelete

urlpatterns = [
    path('funcionarios_list/', FuncionarioList.as_view(), name='funcionarios_list'),
    path('funcionarios_detail/<int:pk>/', FuncionarioDetail.as_view(), name='funcionarios_detail'),
    path('funcionarios_create/', FuncionarioCreate.as_view(), name='funcionarios_create'),
    path('funcionarios_update/<int:pk>/', FuncionarioUpdate.as_view(), name='funcionarios_update'),
    path('funcionarios_delete/<int:pk>/', FuncionarioDelete.as_view(), name='funcionarios_delete'),
]