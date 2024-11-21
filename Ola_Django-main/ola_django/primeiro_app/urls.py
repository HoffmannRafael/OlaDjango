from django.urls import path
from django.http import HttpResponse
from .views import *
# PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView, PessoaDeleteView

def oiDjango(resquest):
    return HttpResponse('Olá primeiroAPP')

urlpatterns = [
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('listar_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoas/<int:pk>/editar/', PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('pessoas/<int:pk>/', PessoaDetailView.as_view(), name='detalhe_pessoa'),
    path('deletar_pessoas/<int:pk>/', PessoaDeleteView.as_view(), name='deletar_pessoa'),
    path('investimentos/', listar_investimentos, name='listar_investimentos'),
    path('investimentos/<int:pk>/', detalhes_investimento, name='detalhes_investimento'),
    path('investimentos/criar/', criar_investimento, name='criar_investimento'),
    path('investimentos/<int:pk>/editar/', editar_investimento, name='editar_investimento'),
    path('investimentos/<int:pk>/deletar/', deletar_investimento, name='deletar_investimento'),
]
