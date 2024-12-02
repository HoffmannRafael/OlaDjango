from django.urls import path
from django.http import HttpResponse
from .views import *
from . import views
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
    path('despesas/', views.DespesaListView.as_view(), name='despesa-list'),
    path('despesas/add/', views.DespesaCreateView.as_view(), name='despesa-add'),
    path('despesas/<int:pk>/edit/', views.DespesaUpdateView.as_view(), name='despesa-edit'),
    path('despesas/<int:pk>/delete/', views.DespesaDeleteView.as_view(), name='despesa-delete'),
    path('perfil-economia/', views.PerfilEconomiaListView.as_view(), name='perfil-economia-list'),
    path('perfil-economia/add/', views.PerfilEconomiaCreateView.as_view(), name='perfil-economia-add'),
    path('perfil-economia/<int:pk>/edit/', views.PerfilEconomiaUpdateView.as_view(), name='perfil-economia-edit'),
    path('perfil-economia/<int:pk>/delete/', views.PerfilEconomiaDeleteView.as_view(), name='perfil-economia-delete'),
]
