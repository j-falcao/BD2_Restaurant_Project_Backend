import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return None

        try:
            validated_token = self.get_validated_token(token)
            print(self.get_user(validated_token), validated_token)
            return self.get_user(validated_token), validated_token
        except AuthenticationFailed:
            return None

    def authenticate_header(self, request):
        return 'Bearer'
