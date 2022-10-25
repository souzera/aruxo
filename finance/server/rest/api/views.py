from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

# MODELS
    ## categoria - **
    ## Contas - **
    ## instituições - **
    ## tipoconta - **
    ## transacoes - **



def index(request):
    return HttpResponse('Olá Mundo')

## Categoria

def details_categoria(request, categoria_id):
    from .models import Categoria
    categoria = Categoria.objects.get(pk=categoria_id)
    return JsonResponse({'categoria':categoria_id,'data':categoria.get_data_dict()})

def results_categoria(request):
    from .models import Categoria
    categoria_list = Categoria.objects.order_by('nome')
    data = [categoria.get_data_dict() for categoria in categoria_list]
    return JsonResponse({'data': data})

## Tipo Conta

def detail_type_cc(request, tipo_conta_id):
    from .models import TipoConta
    tipo_conta = TipoConta.objects.get(pk=tipo_conta_id)
    return JsonResponse({'conta': tipo_conta_id, 'data' : tipo_conta.get_data_dict()})

def cc_types_results(request):
    from .models import TipoConta
    type_cc_list = TipoConta.objects.order_by('nome')
    data = [tipo_cc.get_data_dict() for tipo_cc in type_cc_list]
    return JsonResponse({'data': data})

## Instituições

def detail_instituicao(request, instituicao_id):
    from .models import Instituicao
    instituicao = Instituicao.objects.get(pk=instituicao_id)
    return JsonResponse({'instituicao': instituicao_id, 'data': instituicao.get_data_dict()})

def instituicao_results(request):
    from .models import Instituicao
    instituicao_list = Instituicao.objects.order_by('nome')
    data = [instituicao.get_data_dict() for instituicao in instituicao_list]
    return JsonResponse({'data': data})

## Contas

def detail_conta(request, conta_id):
    from .models import Conta
    transacao = Conta.objects.get(pk=conta_id)
    return JsonResponse({"conta": conta_id, 'data': transacao.get_data_dict()})


def conta_results(request):
    from .models import Conta
    conta_list = Conta.objects.order_by("nome")
    data = [conta.get_data_dict() for conta in conta_list]
    return JsonResponse({'data': data})


## Transações

def detail_transacao(request, transacao_id):
    from .models import Transacao
    transacao = Transacao.objects.get(pk=transacao_id)
    return JsonResponse({"transacao":transacao_id, 'data':transacao.get_data_dict()})

def transacao_results(request):
    from .models import Transacao
    transacao_list = Transacao.objects.order_by("data")
    data = [transacao.get_data_dict() for transacao in transacao_list]
    return JsonResponse({'data':data})



