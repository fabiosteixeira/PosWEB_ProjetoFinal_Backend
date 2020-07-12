from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime, timedelta
import jwt
import json

from ..models import RetornoRequest, User
from ..utils.utils import JWT_ALGORITHM, JWT_EXP_DELTA_SECONDS, JWT_SECRET

@require_http_methods(["POST"])   
@csrf_exempt
def login(request):
    body = json.loads(request.body.decode('utf-8'))

    try:
        user = User.objects.get(email=body['email'])
        user.match_password(body['password'])
    except (User.DoesNotExist, User.PasswordDoesNotMatch):
        return JsonResponse(RetornoRequest(True, "Credenciais inválidas.").as_json())

    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }    
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)

    return JsonResponse({'eherro': False, 
                          'token': jwt_token.decode('utf-8')})