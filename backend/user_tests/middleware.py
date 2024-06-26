from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from organizations.models import Token

class TokenAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if  'register' in request.path or 'login' in request.path or request.path.startswith('/admin/') or 'invite' in request.path:
            return None

        token = request.COOKIES.get('auth_token')
        if not token:
            return JsonResponse({'error': 'Token missing'}, status=401)

        try:
            token = Token.objects.get(key=token)
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Token expired'}, status=401)

        return None
