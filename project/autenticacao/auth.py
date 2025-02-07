from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return None

        try:
            validated_token = self.get_validated_token(token)
            utilizador = Utilizadores.fetch_by_id(self.get_user(validated_token).id)
            utilizador['cargo'] = Cargos.fetch_by_id(utilizador['id_cargo'])

            return utilizador, validated_token
        except AuthenticationFailed:
            return None

    def authenticate_header(self, request):
        return 'Bearer'
    


