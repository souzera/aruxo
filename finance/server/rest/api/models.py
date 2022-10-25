import json

from django.db import models

# Create your models here.

class TipoConta(models.Model):
    nome = models.CharField(max_length=32)
    icon = models.FileField(upload_to='./uploads/cc_type/')
    number_ref = models.BigIntegerField()

    def __str__(self):
        return f' {self.nome}'

    def get_data_dict(self):
        return {
            'nome' : self.nome,
            'icon' : self.icon.url,
            'number_ref' : self.number_ref
            }

class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    icone = models.FileField(upload_to='./uploads/bb_logo/')
    cor_primaria = models.CharField(max_length=6)

    def __str__(self):
        return f' {self.nome}'

    def get_data_dict(self):
        return {
            'nome':self.nome,
            'icone':self.icone.url,
            'cor_primaria': f'#{self.cor_primaria}'
        }

class Conta(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=784)
    tipo = models.ForeignKey(TipoConta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao}'

    def get_data_dict(self):
        return {
            'instituicao':self.instituicao.get_data_dict(),
            'descricao':self.descricao,
            'tipo':self.tipo.get_data_dict()
        }

class Categoria(models.Model):
    nome = models.CharField(max_length=32)
    icone = models.FileField(upload_to='./uploads/cat_type/')

    def __str__(self):
        return f'{self.nome}'

    def get_data_dict(self):
        return {
            'nome': self.nome,
            'icone':self.icone.url
        }

#ENUM
class TipoTransacao(models.TextChoices):

    RECEITA = 'RC','Receita'
    DESPESA = 'DP','Despesa'

class Transacao(models.Model):

    data = models.DateField(auto_now=True)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.FloatField()
    status = models.BooleanField()
    # anexos - comprovantes, vias, etc
    anexos = models.FileField(upload_to='./uploads/anexos/%Y/%m/%d/', blank=True)
    # tipo - (receita ou despesa)
    tipo = models.CharField(max_length=2, choices=TipoTransacao.choices)

    def __str__(self):
        return f"Data: {self.data} \t Descrição: {self.descricao}"

    def get_data_dict(self):
        return {
            'data': self.data,
            'descricao': self.descricao,
            'categoria':self.categoria.get_data_dict(),
            'conta': self.conta.get_data_dict(),
            'valor':self.valor,
            'status':self.status,
            'tipo':self.tipo,
            'anexos': self.anexos.name
        }


