from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

# MODELS
    ## categoria
    ## Contas
    ## instituições
    ## tipoconta
    ## transacoes



def index(request):
    from .models import TipoConta
    type_cc_list = TipoConta.objects.order_by('nome')
    data = [tipo_cc.get_data_dict() for tipo_cc in type_cc_list]
    return JsonResponse({'data':data})

def detail(request, tipo_conta_id):
    from .models import TipoConta
    tipo_conta = TipoConta.objects.get(pk=tipo_conta_id)
    return JsonResponse({'conta': tipo_conta_id, 'data' : tipo_conta.get_data_dict()})

def results(request):
    return HttpResponse(f'todas as contas')



