from django.http import JsonResponse, Http404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from .models import Utilizadores
from . import db
from .serializers import UtilizadoresSerializer, CargosSerializer, UtilizadoresCargosSerializer

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


# UTILIZADORES
@api_view(['GET'])
def get_all_utilizadores_view(request):
    utilizadores = db.get_all_utilizadores()
    serializer = UtilizadoresSerializer(utilizadores, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_utilizador_by_username_view(request, username):
    utilizador = db.get_utilizador_by_username(username)
    if not utilizador:
        raise Http404("Utilizador not found")
    serializer = UtilizadoresSerializer(utilizador)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_utilizador_by_id_view(request, id_utilizador):
    utilizador = db.get_utilizador_by_id(id_utilizador)
    if not utilizador:
        raise Http404("Utilizador not found")
    serializer = UtilizadoresSerializer(utilizador)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_utilizador_by_email_view(request, email):
    utilizador = db.get_utilizador_by_email(email)
    if not utilizador:
        raise Http404("Utilizador not found")
    serializer = UtilizadoresSerializer(utilizador)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_utilizador_by_telemovel_view(request, telemovel):
    utilizador = db.get_utilizador_by_telemovel(telemovel)
    if not utilizador:
        raise Http404("Utilizador not found")
    serializer = UtilizadoresSerializer(utilizador)
    return JsonResponse(serializer.data, safe=False)


# FILTROS POR CARGO
@api_view(['GET'])
def get_all_cozinheiros_view(request):
    cozinheiros = db.get_all_cozinheiros()
    serializer = UtilizadoresSerializer(cozinheiros, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_all_garcons_view(request):
    garcons = db.get_all_garcons()
    serializer = UtilizadoresSerializer(garcons, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_all_administradores_view(request):
    administradores = db.get_all_administradores()
    serializer = UtilizadoresSerializer(administradores, many=True)
    return JsonResponse(serializer.data, safe=False)


# CARGOS
@api_view(['GET'])
def get_all_cargos_view(request):
    cargos = db.get_all_cargos()
    serializer = CargosSerializer(cargos, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_cargo_by_id_view(request, id_cargo):
    cargo = db.get_cargo_by_id(id_cargo)
    if not cargo:
        raise Http404("Cargo not found")
    serializer = CargosSerializer(cargo)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_cargo_by_designacao_view(request, designacao):
    cargo = db.get_cargo_by_designacao(designacao)
    if not cargo:
        raise Http404("Cargo not found")
    serializer = CargosSerializer(cargo)
    return JsonResponse(serializer.data, safe=False)

# UTILIZADORES CARGOS
@api_view(['GET'])
def get_all_utilizadores_cargos_view(request):
    utilizadores_cargos = db.get_all_utilizadores_cargos()
    serializer = UtilizadoresCargosSerializer(utilizadores_cargos, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_utilizadores_cargos_by_id_utilizador_view(request, id_utilizador):
    utilizadores_cargos = db.get_utilizadores_cargos_by_id_utilizador(id_utilizador)
    serializer = UtilizadoresCargosSerializer(utilizadores_cargos, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_utilizadores_cargos_by_id_cargo_view(request, id_cargo):
    utilizadores_cargos = db.get_utilizadores_cargos_by_id_cargo(id_cargo)
    serializer = UtilizadoresCargosSerializer(utilizadores_cargos, many=True)
    return JsonResponse(serializer.data, safe=False)