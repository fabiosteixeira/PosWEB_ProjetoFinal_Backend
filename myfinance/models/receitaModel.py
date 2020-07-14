from django.db import models

class Receita(models.Model):
    CLASSIFICACAO_CHOICES = (
        ('DT', 'Dívida de terceiros'),
        ('DO', 'Doação'),
        ('SA', 'Salário'),
        ('SP', 'Serviço prestado'),
        ('OU', 'Outros'),
        ('VE', 'Vendas')
    )

    FORMA_RECEBIMENTO_CHOICES = (
        ('B', 'Boleto'),
        ('C', 'Crédito'),
        ('D', 'Débito'),
        ('M', 'Dinheiro'),
        ('P', 'Depósito'),
        ('O', 'Outros')
    )
    
    SITUACAO_CHOICES = (
        ('PR', 'Recebido'),
        ('AR', 'A receber')
    )
    
    id = models.AutoField(primary_key=True)
    classificacao = models.CharField(max_length=255)
    data_expectativa = models.DateField(null=False)
    data_recebimento = models.DateField(null=True)
    descricao = models.CharField(max_length=255)
    formaRecebimento = models.CharField(max_length=1, choices=FORMA_RECEBIMENTO_CHOICES, default='O')
    situacao = models.CharField(max_length=255)
    valor = models.DecimalField(null=False, max_digits=8, decimal_places=2)

    def as_json(self):
        return dict(
            id = self.id
            , classificacao = self.classificacao
            , data_expectativa = self.data_expectativa
            , data_recebimento = self.data_recebimento
            , descricao = self.descricao
            , formaRecebimento = self.formaRecebimento
            , situacao = self.situacao
            , valor = self.valor.__str__()
        )
    