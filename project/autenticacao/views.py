from django.http import JsonResponse, Http404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import db
from .serializers import UtilizadoresSerializer, CargosSerializer, UtilizadoresCargosSerializer, SignupSerializer, LoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )

    if user:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response({"message": "Login successful"}, status=200)

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
        )
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,
        )

        return response

    return Response({"error": "Invalid credentials"}, status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    })

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