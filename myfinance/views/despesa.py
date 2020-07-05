from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

from ..models import Despesa, RetornoRequest
from ..utils import Utils

# GET: retorna a lista de despesas
# POST: cria no banco uma nova despesa
@require_http_methods(["GET", "POST"])   
@csrf_exempt
def despesa(request):
    if(request.method=="GET"):
        despesas = [ob.as_json() for ob in Despesa.objects.all()]
        return HttpResponse(json.dumps(despesas, default=Utils.converter), content_type="application/json")
    elif(request.method=="POST"):
        atualizaDespesa(request, 0)
        return JsonResponse(RetornoRequest(False, "Objeto criado com sucesso.").as_json())


# GET: retorna dados de uma despesa
# POST: atualiza no banco a despesa de ID = id_despesa
# DELETE: deleta do banco a despesa de ID = id_despesa
@require_http_methods(["GET", "POST", "DELETE"])  
@csrf_exempt
def despesaOp(request, id_despesa):
    despesa = None
    try:
        despesa = Despesa.objects.get(id=id_despesa)
    except ObjectDoesNotExist:
        return JsonResponse(RetornoRequest(True, "Objeto não encontrado.").as_json())

    if(request.method=="GET"):
        context = {}
        if(despesa):
            return JsonResponse(despesa.as_json())   

    elif(request.method=="POST"):
        if(despesa):
            atualizaDespesa(request, id_despesa)
            return JsonResponse(RetornoRequest(False, "Objeto atualizado com sucesso.").as_json())

    elif(request.method=="DELETE"):
        jsonReturn = RetornoRequest(True, "Não foi possível excluir o objeto.").as_json()
        if(despesa):
            despesa.delete()
            jsonReturn = RetornoRequest(False, "Objeto excluído com sucesso.").as_json()
        
        return JsonResponse(jsonReturn)

# atualiza as informações de uma despesa existente
def atualizaDespesa(request, id_despesa):
    body = json.loads(request.body.decode('utf-8'))
    dataPagamento = body['data_pagamento']

    if(dataPagamento == ""):
        dataPagamento = None

    despesa = Despesa(classificacao=body['classificacao'],
                      data_pagamento=dataPagamento,
                      data_vencimento=body['data_vencimento'],
                      descricao=body['descricao'],
                      formaPagamento=body['formaPagamento'],
                      situacao=body['situacao'],
                      valor=body['valor']
                    )

    if (id_despesa > 0):
        despesa.id = id_despesa

    print("Atualizando despesa de id: " + str(id_despesa))
    despesa.save()
