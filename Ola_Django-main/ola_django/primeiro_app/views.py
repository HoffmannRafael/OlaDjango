from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Pessoa, InteracoesPessoa, Meta
from .forms import PessoaCreateForm, PessoaUpdateForm, FormDeletePessoa, MetaForm
from django.contrib import messages

#criação da tela de cadastro de pessoa
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaCreateForm
    template_name = 'cadastrar_pessoa.html'
    success_url = reverse_lazy('lista_pessoas')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        InteracoesPessoa.objects.create(
            pessoa = self.object,
            mensagem = form.cleaned_data['interacao']
            )
        
        messages.success(self.request, 'Pessoa cadastrada com sucesso!')
        return response

class PessoaListView(ListView):
    model = Pessoa 
    template_name = 'lista_pessoas.html'

class PessoaUpdateView(UpdateView):
    model= Pessoa
    template_name = "editar_pessoa.html"
    form_class = PessoaUpdateForm
    success_url = reverse_lazy('lista_pessoas')

    def form_valid(self, form):
        response = super().form_valid(form)
        if(form.cleaned_data['interacao'] != ''):
            InteracoesPessoa.objects.create(
                pessoa = self.object,
                mensagem = form.cleaned_data['interacao']
                )
        
        messages.success(self.request, 'Pessoa cadastrada com sucesso!')
        return response

class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = "detalhe_pessoa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pessoa = self.object
        interacoes = InteracoesPessoa.objects.filter(pessoa=pessoa)
        interacoes_formatada = [{
            'data_hora': interacao.data_hora.strftime('%d/%m/%Y %H:%M'),
            'mensagem': interacao.mensagem
            }
            for interacao in interacoes
        ]
        context['interacoes_formatada'] = interacoes_formatada

        return context

class PessoaDeleteView(DeleteView):
    model = Pessoa
    form_class = FormDeletePessoa
    template_name = "deletar_pessoa.html"
    success_url = reverse_lazy('lista_pessoas')
    
    
# Lista todas as metas
from django.views.generic import ListView
from .models import Meta

class MetaListView(ListView):
    model = Meta
    form_class = MetaForm
    template_name = 'meta_list.html'
    context_object_name = 'meta'


# Detalhes de uma meta específica
class MetaDetailView(DetailView):
    model = Meta
    template_name = 'meta/meta_detail.html'
    context_object_name = 'meta'

# Cria uma nova meta
class MetaCreateView(CreateView):
    model = Meta
    form_class = MetaForm
    template_name = 'meta_form.html'
    success_url = reverse_lazy('meta-list')

    def form_valid(self, form):
        # Configura o dono da meta como a pessoa logada, se necessário
        form.instance.pessoa = self.request.user
        return super().form_valid(form)

# Atualiza uma meta existente
class MetaUpdateView(UpdateView):
    model = Meta
    form_class = MetaForm
    template_name = 'meta/meta_form.html'
    success_url = reverse_lazy('meta-list')

# Deleta uma meta
class MetaDeleteView(DeleteView):
    model = Meta
    template_name = 'meta/meta_confirm_delete.html'
    success_url = reverse_lazy('meta-list')
