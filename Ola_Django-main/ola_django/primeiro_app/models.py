from django.db import models
from django import forms

class TipoPessoa(models.Model):
    nome = models.CharField(max_length=45) 
    descricao = models.CharField(max_length=60, blank=True, null=True)  

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    email = models.CharField(max_length=60)
    tipo_pessoa = models.ForeignKey(TipoPessoa, on_delete=models.PROTECT)  
    def __str__(self):
        return self.nome


class InteracoesPessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()

    def __str__(self):
        return f"Interação com {self.pessoa.nome} em {self.data_hora}"


class Meta(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.TextField()
    valor = models.FloatField()
    valor_atual = models.FloatField(default=0)  
    data_inicial = models.DateField()
    data_final = models.DateField()

    @property
    def progresso(self):
        """Calcula o progresso como uma porcentagem."""
        if self.valor == 0:
            return 0
        return min((self.valor_atual / self.valor) * 100, 100) 
    
class Despesa(models.Model):
    CATEGORIAS = [
        ('Fixa', 'Despesa Fixa'),
        ('Variavel', 'Despesa Variável'),
        ('Geral', 'Despesa Geral'),
        ('Investimento', 'Investimento'),
        ('Operacionais', 'Despesas operacionais'),
        ('Não Operacionais', 'Despesas Não operacionais')
    ]

    categoria = models.CharField(max_length=255, choices=CATEGORIAS)
    valor = models.FloatField()
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.valor}"

class PerfilEconomia(models.Model):
    TIPOS_ECONOMIA = [
        ('Passiva', 'Economia Passiva'),
        ('Agressiva', 'Economia Agressiva')
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPOS_ECONOMIA)
    porcentagem_despesa_fixa = models.FloatField()
    porcentagem_despesa_variavel = models.FloatField()
    porcentagem_despesa_geral = models.FloatField()
    porcentagem_investimento = models.FloatField()
    ajuste_automatico = models.BooleanField(default=True)

class PerfilEconomiaForm(forms.ModelForm):
    class meta:
        model = PerfilEconomia
        fields = ['tipo', 'ajuste_automático']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.isinstance.ajuste_automatico:
            self.fields['tipo'].widget = forms.HiddenInput()

    
    def ajustar_tipo_economia(self, renda_mensal):
        despesas_fixas = Despesa.objects.filter(categoria="Fixa").aggregate(models.Sum('valor'))['valor_sum'] or 0
        despesas_variaveis = Despesa.objects.filter(categoria="Variavel").aggregate(models.Sum('valor'))['valor_sum'] or 0
        total_despesas = despesas_fixas + despesas_variaveis
        
        porcentagem_total_despesas = (total_despesas / renda_mensal) * 100

        if porcentagem_total_despesas > 75:
            self.tipo = 'Passiva'
            self.porcentagem_despesa_fixa = 50.0
            self.porcentagem_despesa_variavel = 5.0
            self.porcentagem_despesa_geral = 5.0
            self.porcentagem_investimento = 10.0
        else:
            self.tipo = 'Agressiva'
            self.porcentagem_despesa_fixa = 40.0
            self.porcentagem_despesa_variavel = 15.0
            self.porcentagem_despesa_geral = 5.0
            self.porcentagem_investimento = 30.0

    def __str__(self):
        return f"{self.tipo} - Despesas F: {self.porcentagem_despesa_fixa}% Var: {self.porcentagem_despesa_variavel}% Geral: {self.porcentagem_despesa_geral}% Invest: {self.porcentagem_investimento}%"

class Investimentos(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.FloatField()
    prazo = models.DateField()
    frequencia = models.FloatField()
    def __str__(self):
        return f"[{self.pessoa.nome}] Investimento de R${self.valor} de frequência {self.frequencia} com prazo de encerramento em {self.prazo}."
