from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import *
from .bd.operacoes import *


@api_view(['POST'])
def signup_view(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["POST"])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        utilizador = Utilizadores.objects.filter(username=username).first()

        if utilizador and check_password(password, utilizador.password):
            refresh = RefreshToken.for_user(utilizador)

            response = Response({"message": "Login successful"}, status=200)

            response.set_cookie(
                "access_token",
                str(refresh.access_token),
                httponly=True,
                secure=True
            )

            response.set_cookie(
                "refresh_token",
                str(refresh),
                httponly=True,
                secure=True
            )

            return response

    return Response({"error": "Credenciais inválidas"}, status=401)

@api_view(['GET'])
def get_all_utilizadores_view(request):
    return Response(Utilizadores.fetch_all())

@api_view(['GET'])
def get_garcons_view(request):
    return Response(Utilizadores.fetch_all_garcons())

@api_view(['GET'])
def get_administradores_view(request):
    return Response(Utilizadores.fetch_all_administradores())

@api_view(['GET'])
def get_cozinheiros_view(request):
    return Response(Utilizadores.fetch_all_cozinheiros())

@api_view(['GET'])
def mee_bd_view(request):
    return Response(mee_bd())


# CARGOS
