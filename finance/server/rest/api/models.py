from django.db import models

# Create your models here.

class TipoConta(models.Model):
    nome = models.CharField(max_length=32)
    icon = models.FileField()
    number_ref = models.BigIntegerField()

class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    icone = models.FileField()
    cor_primaria = models.CharField(max_length=6)

class Conta(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=784)
    tipo = models.ForeignKey(TipoConta, on_delete=models.CASCADE)

class Categoria(models.Model):
    nome = models.CharField(max_length=32)
    icone = models.FileField()

class Transacao(models.Model):
    data = models.DateField(auto_now=True)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.FloatField()
    status = models.BooleanField()
    anexos = models.FileField()
    tipo = models.BigIntegerField()


