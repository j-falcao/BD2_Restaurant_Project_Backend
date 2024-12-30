from rest_framework import serializers
from .models import Cargos, Utilizadores, UtilizadoresCargos
from django.contrib.auth.hashers import make_password
from .db import *

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilizadores
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_superuser'] = False
        return create_utilizador(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = '__all__'

class UtilizadoresSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Utilizadores
        fields = '__all__'

class UtilizadoresCargosSerializer(serializers.ModelSerializer):
    id_utilizador = UtilizadoresSerializer(read_only=True)
    id_cargo = CargosSerializer(read_only=True)

    class Meta:
        model = UtilizadoresCargos
        fields = '__all__'
