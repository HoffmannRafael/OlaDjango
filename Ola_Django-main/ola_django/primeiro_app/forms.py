from django import forms
from .models import Pessoa, Investimentos

class PessoaCreateForm(forms.ModelForm):
    interacao = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Pessoa
        fields = '__all__' # alternativa para usar todos os campos -> '__all__'
        
class PessoaUpdateForm(forms.ModelForm):
        interacao = forms.CharField(widget=forms.Textarea)
        class Meta:
            model = Pessoa
            fields = '__all__'
    
class FormDeletePessoa(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [] #Nenhum campo

class InvestimentoForm(forms.ModelForm):
    class Meta:
        model = Investimentos
        fields = ['pessoa', 'valor', 'prazo', 'frequencia']