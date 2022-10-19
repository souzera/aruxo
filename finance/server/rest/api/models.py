from django.db import models

# Create your models here.

class TipoConta(models.Model):
    nome = models.CharField(max_length=32)
    icon = models.FileField()
    number_ref = models.BigIntegerField()

    def __str__(self):
        return f'Tipo: {self.nome}'

    def get_data_dict(self):
        return {
            'nome' : self.nome,
            'icon' : self.icon,
            'number_ref' : self.number_ref
        }

class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    icone = models.FileField()
    cor_primaria = models.CharField(max_length=6)

    def __str__(self):
        return f'Instituição: {self.nome}'

    def get_data_dict(self):
        return {
            'nome':self.nome,
            'icone':self.icone,
            'cor_primaria': f'#{self.cor_primaria}'
        }

class Conta(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=784)
    tipo = models.ForeignKey(TipoConta, on_delete=models.CASCADE)

    def __str__(self):
        return f'Instituição: {self.instituicao}' \
               f'\n \t {self.descricao}' \
               f'\n \t Tipo: {self.tipo}'

    def get_data_dict(self):
        return {
            'instituicao':self.instituicao.get_data_dict(),
            'descricao':self.descricao,
            'tipo':self.tipo.get_data_dict()
        }

class Categoria(models.Model):
    nome = models.CharField(max_length=32)
    icone = models.FileField()

    def __str__(self):
        return f'{self.nome}'

    def get_data_dict(self):
        return {
            'nome': self.nome,
            'icone':self.icone
        }

class Transacao(models.Model):
    data = models.DateField(auto_now=True)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.FloatField()
    status = models.BooleanField()
    # anexos - comprovantes, vias, etc
    anexos = models.FileField()
    # tipo - (receita ou despesa)
    tipo = models.BigIntegerField()

    def __str__(self):
        return f"Data: {self.data}' \
               f'\t Descrição: {self.descricao}' \
               f'\n Categoria: {self.categoria} \t CC.: {self.conta}' \
               f'\n Valor: {self.valor} Status: {self.status}" \
               f"\n Tipo: {self.tipo} \n {self.anexos}"

    def get_data_dict(self):
        return {
            'data': self.data,
            'descricao': self.descricao,
            'categoria':self.categoria.get_data_dict(),
            'conta': self.conta.get_data_dict(),
            'valor':self.valor,
            'status':self.status,
            'anexos':self.anexos,
            'tipo':self.tipo
        }


