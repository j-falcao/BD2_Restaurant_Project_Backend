from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from .models import Utilizadores


@api_view(['POST'])
def signup_view(request):
    """
    Handle user signup and return a success message.
    """
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not all([username, email, password]):
        return JsonResponse({"error": "Todos os campos devem ser preenchidos"}, status=400)

    if Utilizadores.objects.filter(username=username).exists():
        return JsonResponse({"error": "Nome de utilizador já existe"}, status=400)
    
    if Utilizadores.objects.filter(email=email).exists():
        return JsonResponse({"error": "Email já registrado"}, status=400)

    # Hash the password before saving the user
    hashed_password = make_password(password)
    user = Utilizadores.objects.create(username=username, email=email, password=hashed_password)

    if user:
        return JsonResponse({"message": "Utilizador criado com sucesso"})
    else:
        return JsonResponse({"error": "Erro ao criar o utilizador"}, status=500)


@api_view(['POST'])
def login_view(request):
    """
    Handle user login and return JWT in an HTTP-only cookie.
    """
    username = request.data.get("username")
    password = request.data.get("password")

    if not all([username, password]):
        return JsonResponse({"error": "Todos os campos devem ser preenchidos"}, status=400)


    # Verificar as credenciais
    user = Utilizadores.objects.get(username=username)
    if not check_password(password, user.password):
        return JsonResponse({"error": "Credenciais inválidas"}, status=401)

    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Set the access token as an HTTP-only cookie
    response = JsonResponse({"message": "Login bem-sucedido"})
    response.set_cookie(
        "access_token",
        access_token,
        httponly=True,
        secure=True,
        samesite="Strict"
    )
    return response


@api_view(['GET'])
def whoami_view(request):
    """
    Identify the authenticated user from the JWT cookie.
    """
    access_token = request.COOKIES.get("access_token")
    if not access_token:
        return JsonResponse({"error": "Utilizador não autenticado"}, status=401)

    try:
        # Decode the JWT token to get the user info
        refresh = RefreshToken(token=access_token)
        user_id = refresh["user_id"]
        user = Utilizadores.objects.get(id=user_id)
        return JsonResponse({"username": Utilizadores.username})
    except Exception:
        return JsonResponse({"error": "Token inválido ou expirado"}, status=401)
