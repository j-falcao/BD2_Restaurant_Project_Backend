from rest_framework import serializers
from .bd.operacoes import *
from .utils import hash_password, check_password

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    id_cargo = serializers.IntegerField()
    url_imagem = serializers.URLField()
    is_superuser = serializers.BooleanField(default=False)

    def create(self, validated_data):
        validated_data['password'] = hash_password(validated_data['password'])
        validated_data['is_superuser'] = False
        return create_utilizador(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data["username"]
        password = data["password"]

        with connection.cursor() as cursor:
            cursor.execute("SELECT id, password FROM utilizadores WHERE username = %s", [username])
            row = cursor.fetchone()

            if not row or not check_password(password, row[1]):
                raise serializers.ValidationError("Invalid credentials")

        return data