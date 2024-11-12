from django import forms
from .models import Pessoa
from .models import Meta

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
        
class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ['titulo', 'valor', 'data_inicial', 'data_final']
