import jwt
from django.conf import settings
from django.http import JsonResponse

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        request_path = request.path_info
        if request_path.startswith('/login'):
            return None

        authorization_header = request.headers.get('Authorization')

        if authorization_header and authorization_header.startswith('Bearer '):
            jwt_token = authorization_header.split(' ')[1]

            try:
                decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token has expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'error': 'Invalid token'}, status=401)

        else:
            return JsonResponse({'error': 'Invalid authorization header'}, status=401)
        return None
