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
