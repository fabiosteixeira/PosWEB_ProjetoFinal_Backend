from django.http import JsonResponse
import json
import jwt

from .models import RetornoRequest, User
from .utils.utils import JWT_ALGORITHM, JWT_EXP_DELTA_SECONDS, JWT_SECRET

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.path.startswith('/login/'):
            request.user = None
            print('Entrou aqui!!')
            jwt_token = request.headers.get('authorization', None)
            if jwt_token:
                try:
                    payload = jwt.decode(jwt_token, JWT_SECRET,
                                        algorithms=[JWT_ALGORITHM])
                except (jwt.DecodeError, jwt.ExpiredSignatureError):
                    return JsonResponse(RetornoRequest(True, "Token inválido.").as_json())
                request.user = User.objects.get(id=payload['user_id'])
            else:
                return JsonResponse(RetornoRequest(True, "Autenticação requerida.").as_json())

        response = self.get_response(request)
        return response