from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Pessoa, InteracoesPessoa, Investimentos, Despesa, PerfilEconomia
from .forms import PessoaCreateForm, PessoaUpdateForm, FormDeletePessoa, InvestimentoForm
from django.contrib import messages
# Create your views here.
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

def listar_investimentos(request):
    investimentos = Investimentos.objects.all()
    return render(request, 'investimentos/listar.html', {'investimentos': investimentos})

def detalhes_investimento(request, pk):
    investimento = get_object_or_404(Investimentos, pk=pk)
    return render(request, 'investimentos/detalhes.html', {'investimento': investimento})

def criar_investimento(request):
    if request.method == 'POST':
        form = InvestimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('listar_investimentos'))
    else:
        form = InvestimentoForm()
    return render(request, 'investimentos/form.html', {'form': form})

def editar_investimento(request, pk):
    investimento = get_object_or_404(Investimentos, pk=pk)
    if request.method == 'POST':
        form = InvestimentoForm(request.POST, instance=investimento)
        if form.is_valid():
            form.save()
            return redirect(reverse('listar_investimentos'))
    else:
        form = InvestimentoForm(instance=investimento)
    return render(request, 'investimentos/form.html', {'form': form})

def deletar_investimento(request, pk):
    investimento = get_object_or_404(Investimentos, pk=pk)
    if request.method == 'POST':
        investimento.delete()
        return redirect(reverse('listar_investimentos'))
    return render(request, 'investimentos/confirmar_delete.html', {'investimento': investimento})

# Views para Despesa
class DespesaListView(ListView):
    model = Despesa
    template_name = 'despesa_list.html'
    context_object_name = 'despesas'

class DespesaCreateView(CreateView):
    model = Despesa
    fields = ['categoria', 'valor', 'descricao']
    template_name = 'despesa_form.html'
    success_url = reverse_lazy('despesa-list')

class DespesaUpdateView(UpdateView):
    model = Despesa
    fields = ['categoria', 'valor', 'descricao']
    template_name = 'despesa_form.html'
    success_url = reverse_lazy('despesa-list')

class DespesaDeleteView(DeleteView):
    model = Despesa
    template_name = 'despesa_confirm_delete.html'
    success_url = reverse_lazy('despesa-list')

# Views para PerfilEconomia
class PerfilEconomiaListView(ListView):
    model = PerfilEconomia
    template_name = 'perfil_economia_list.html'
    context_object_name = 'perfis'

class PerfilEconomiaCreateView(CreateView):
    model = PerfilEconomia
    fields = ['tipo', 'ajuste_automatico', 'porcentagem_despesa_fixa', 'porcentagem_despesa_variavel', 'porcentagem_despesa_geral', 'porcentagem_investimento']
    template_name = 'perfil_economia_form.html'
    success_url = reverse_lazy('perfil-economia-list')

class PerfilEconomiaUpdateView(UpdateView):
    model = PerfilEconomia
    fields = ['tipo', 'ajuste_automatico', 'porcentagem_despesa_fixa', 'porcentagem_despesa_variavel', 'porcentagem_despesa_geral', 'porcentagem_investimento']
    template_name = 'perfil_economia_form.html'
    success_url = reverse_lazy('perfil-economia-list')

class PerfilEconomiaDeleteView(DeleteView):
    model = PerfilEconomia
    template_name = 'perfil_economia_confirm_delete.html'
    success_url = reverse_lazy('perfil-economia-list')