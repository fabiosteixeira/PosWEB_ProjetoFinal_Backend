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
            jwt_token = request.headers.get('authorization', None)
            if jwt_token:
                try:
                    payload = jwt.decode(jwt_token, JWT_SECRET,
                                        algorithms=[JWT_ALGORITHM])
                except (jwt.DecodeError, jwt.ExpiredSignatureError):
                    return JsonResponse({'message': 'Token inválido'},
                                        status=400)
                request.user = User.objects.get(id=payload['user_id'])
            else:
                return JsonResponse({'message': 'Autenticação requerida'},
                                            status=401) 

        response = self.get_response(request)
        return response