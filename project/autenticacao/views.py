from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .models import Utilizadores

@api_view(['POST'])
def signup_view(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not all([username, email, password]):
        return JsonResponse({"error": "Todos os campos devem ser preenchidos"}, status = 400)
    
    user = Utilizadores.objects.create_user(username, email, password)

    if user is not None:
        return JsonResponse({"message": "Utilizador criado com sucesso"})
    else:
        return JsonResponse({"error": "Erro ao criar o utilizador"}, status = 500)

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    print(username, password)
    
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
    

@api_view(['GET'])
def whoami_view(request):
    # Verificar se o utilizador está autenticado
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return JsonResponse({"username": request.user.username})
    else:
        return JsonResponse({"error": "Utilizador não autenticado"})