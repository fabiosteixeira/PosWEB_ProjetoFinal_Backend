from django.views.decorators.http import require_http_methods
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

from ..models import User, RetornoRequest
from ..utils import Utils

@require_http_methods(["GET", "POST"])   
@csrf_exempt
def user(request):
    if(request.method=="GET"):
        user = [ob.as_json() for ob in User.objects.all()]
        return HttpResponse(json.dumps(user, default=Utils.converter), content_type="application/json")
    elif(request.method=="POST"):
        atualizaUser(request, 0)
        return JsonResponse(RetornoRequest(False, "Objeto criado com sucesso.").as_json())


@require_http_methods(["GET", "POST", "DELETE"])  
@csrf_exempt
def userOp(request, id_user):
    user = None
    try:
        user = User.objects.get(id=id_user)
    except ObjectDoesNotExist:
        return JsonResponse(RetornoRequest(True, "Objeto não encontrado.").as_json())

    if(request.method=="GET"):
        context = {}
        if(user):
            return JsonResponse(user.as_json())   

    elif(request.method=="POST"):
        if(user):
            atualizaUser(request, id_user)
            return JsonResponse(RetornoRequest(False, "Objeto atualizado com sucesso.").as_json())

    elif(request.method=="DELETE"):
        jsonReturn = RetornoRequest(True, "Não foi possível excluir o objeto.").as_json()
        if(user):
            user.delete()
            jsonReturn = RetornoRequest(False, "Objeto excluído com sucesso.").as_json()
        return JsonResponse(jsonReturn)

def atualizaUser(request, id_user):
    body = json.loads(request.body.decode('utf-8'))

    user = User(nome=body['nome'],
                email=body['email'],
                password=body['password']
                )

    if (id_user > 0):
        user.id = id_user

    user.save()
    return user

@require_http_methods(["POST"])   
@csrf_exempt
def userCreateExterno(request):
    try:
        user = atualizaUser(request, 0)
    except (User.DoesNotExist, User.PasswordDoesNotMatch):
        return JsonResponse(RetornoRequest(True, "Não foi possível cadastrar o novo usuário.").as_json())
    
    return JsonResponse({'eherro': False, 
                         'id': user.id,
                         'username': user.email,
                         'name': user.nome})
