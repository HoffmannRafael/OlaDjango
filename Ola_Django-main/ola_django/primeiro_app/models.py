from django.db import models

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

    
    
    