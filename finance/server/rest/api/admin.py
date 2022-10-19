from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(TipoConta)
admin.site.register(Instituicao)
admin.site.register(Categoria)
admin.site.register(Conta)
admin.site.register(Transacao)
