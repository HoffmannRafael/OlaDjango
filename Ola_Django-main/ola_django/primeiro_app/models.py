from django.db import models

# Model for different types of people (e.g., customer, supplier, etc.)
class TipoPessoa(models.Model):
    nome = models.CharField(max_length=45)  # e.g., "Cliente", "Fornecedor"
    descricao = models.CharField(max_length=60, blank=True, null=True)  # Optional description

    def __str__(self):
        return self.nome

# Model for a person with a foreign key to TipoPessoa
class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    email = models.CharField(max_length=60)
    tipo_pessoa = models.ForeignKey(TipoPessoa, on_delete=models.PROTECT)  # Prevent deletion if related
    def __str__(self):
        return self.nome

# Model for interactions related to a person
class InteracoesPessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()

    def __str__(self):
        return f"Interação com {self.pessoa.nome} em {self.data_hora}"
    
class Despesa(models.Model):
    CATEGORIAS = [
        ('Fixa', 'Despesa Fixa'),
        ('Variavel', 'Despesa Variável'),
        ('Geral', 'Despesa Geral'),
        ('Investimento', 'Investimento')
    ]

    categoria = models.CharField(max_length=15, choices=CATEGORIAS)
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

    def __str__(self):
        return f"{self.tipo} - Despesas F: {self.porcentagem_despesa_fixa}% Var: {self.porcentagem_despesa_variavel}% Geral: {self.porcentagem_despesa_geral}% Invest: {self.porcentagem_investimento}%"