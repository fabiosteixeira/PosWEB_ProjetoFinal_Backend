from django.views.decorators.http import require_http_methods
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

from ..models import Receita, RetornoRequest
from ..utils import Utils

# GET: retorna a lista de receitas
# POST: cria no banco uma nova receita
@require_http_methods(["GET", "POST"])   
@csrf_exempt
def receita(request):
    if(request.method=="GET"):
        receitas = [ob.as_json() for ob in Receita.objects.all()]
        return HttpResponse(json.dumps(receitas, default=Utils.converterParaListagem), content_type="application/json")
    elif(request.method=="POST"):
        atualizaReceita(request, 0)
        return JsonResponse(RetornoRequest(False, "Objeto criado com sucesso.").as_json())        
       
# GET: retorna dados de uma receita
# POST: atualiza no banco a receita de ID = id_receita
# DELETE: deleta do banco a receita de ID = id_receita
@require_http_methods(["GET", "POST", "DELETE"])  
@csrf_exempt
def receitaOp(request, id_receita):
    receita = None
    try:
        receita = Receita.objects.get(id=id_receita)
    except ObjectDoesNotExist:
        return JsonResponse(RetornoRequest(True, "Objeto não encontrado.").as_json())

    if(request.method=="GET"):
        context = {}
        if(receita):
            return JsonResponse(receita.as_json())   

    elif(request.method=="POST"):
        if(receita):
            atualizaReceita(request, id_receita)
            return JsonResponse(RetornoRequest(False, "Objeto atualizado com sucesso.").as_json())

    elif(request.method=="DELETE"):
        jsonReturn = RetornoRequest(True, "Não foi possível excluir o objeto.").as_json()
        if(receita):
            receita.delete()
            jsonReturn = RetornoRequest(False, "Objeto excluído com sucesso.").as_json()
        return JsonResponse(jsonReturn)

# atualiza as informações de uma receita existente
def atualizaReceita(request, id_receita):
    body = json.loads(request.body.decode('utf-8'))
    dataRecebimento = body['data_recebimento']

    if(dataRecebimento == "" or dataRecebimento == []):
        dataRecebimento = None

    receita = Receita(classificacao=body['classificacao'],
                      data_recebimento=dataRecebimento,
                      data_expectativa=body['data_expectativa'],
                      descricao=body['descricao'],
                      formaRecebimento=body['formaRecebimento'],
                      situacao=body['situacao'],
                      valor=body['valor']
                    )

    if (id_receita > 0):
        receita.id = id_receita

    receita.save()
