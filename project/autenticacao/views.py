from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import *
from .models import *
from .auth_backends import CustomAuthBackend


@api_view(['POST'])
def signup_view(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        new_user = serializer.save()
        return Response({"message": "User created successfully"}, status=201)
    return Response(serializer.errors, status=400)

@api_view(["POST"])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        with connection.cursor() as cursor:
            cursor.execute("SELECT id_utilizador, password FROM utilizadores WHERE username = %s", [username])
            user = cursor.fetchone()

        if user and check_password(password, user[1]):
            request.session["user_id"] = user[0]  # Guardar o ID do utilizador na sessão
            return Response({"message": "Login successful"}, status=200)

    return Response({"error": "Invalid credentials"}, status=401)


@api_view(["POST"])
def logout_view(request):
    request.session.flush() 
    return Response({"message": "Logged out"}, status=200)



@api_view(['GET'])
def whoami_view(request):
    user = request.user
    return Response({
        "id": user.id_utilizador,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    })

@api_view(['GET'])
def get_all_utilizadores_view(request):
    return Response(Utilizadores.fetch_all())

""" 
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
    return JsonResponse(serializer.data, safe=False) """