from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    # Autenticar o usuário
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        # Gerar o token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Configurar o cookie com o token de acesso
        response = JsonResponse({"message": "Login bem-sucedido"})
        response.set_cookie(
            "access_token",
            access_token,
            httponly=True,
            secure=True,
            samesite="Strict"
        )
        return response
    else:
        return JsonResponse({"error": "Credenciais inválidas"}, status=401)
    