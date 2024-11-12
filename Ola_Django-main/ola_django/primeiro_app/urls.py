from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView,PessoaDeleteView
from .views import MetaListView, MetaDetailView, MetaCreateView, MetaUpdateView, MetaDeleteView

def oiDjango(resquest):
    return HttpResponse('Olá primeiroAPP')

urlpatterns = [
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('listar_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoas/<int:pk>/editar/', PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('pessoas/<int:pk>/', PessoaDetailView.as_view(), name='detalhe_pessoa'),
    path('deletar_pessoas/<int:pk>/', PessoaDeleteView.as_view(), name='deletar_pessoa'),
    path('metas/', MetaListView.as_view(), name='meta-list'),
    path('metas/<int:pk>/', MetaDetailView.as_view(), name='meta-detail'),
    path('metas/nova/', MetaCreateView.as_view(), name='meta-create'),
    path('metas/<int:pk>/editar/', MetaUpdateView.as_view(), name='meta-update'),
    path('metas/<int:pk>/deletar/', MetaDeleteView.as_view(), name='meta-delete'),
]
