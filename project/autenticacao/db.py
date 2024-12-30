from .models import *
from django.db import connection, transaction

def create_utilizador(validated_data):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CALL create_utilizadores(%s, %s, %s, %s, %s, %s, %s) 
            """,
            (
                validated_data.get('username'),
                validated_data.get('first_name'),
                validated_data.get('last_name'),
                validated_data.get('is_superuser'),
                validated_data.get('url_imagem'),
                validated_data.get('password'),
                None
            )
        )
        id_novo_utilizador = cursor.fetchone()[0]

    return get_utilizador_by_id(id_novo_utilizador)

def update_utilizador(id_utilizador, validated_data):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CALL update_utilizadores(%s, %s, %s, %s, %s, %s, %s) 
            """,
            (
                id_utilizador,
                validated_data.get('username'),
                validated_data.get('first_name'),
                validated_data.get('last_name'),
                validated_data.get('is_superuser'),
                validated_data.get('url_imagem'),
                validated_data.get('password'),
            )
        )
        id_utilizador = cursor.fetchone()[0]

    return get_utilizador_by_id(id_utilizador)


def get_all_utilizadores():
    return Utilizadores.objects.all()

def get_utilizador_by_username(username):
    return Utilizadores.objects.filter(username=username).first()

def get_utilizador_by_id(id):
    return Utilizadores.objects.filter(id=id).first()

def get_all_cozinheiros():
    return Utilizadores.objects.filter(cargos__id_cargo=1)

def get_all_garcons():
    return Utilizadores.objects.filter(cargos__id_cargo=2)

def get_all_administradores():
    return Utilizadores.objects.filter(cargos__id_cargo=3)

def get_all_cargos():
    return Cargos.objects.all()

def get_cargo_by_id(id_cargo):
    return Cargos.objects.filter(id_cargo=id_cargo).first()

def get_cargo_by_designacao(designacao):
    return Cargos.objects.filter(designacao=designacao).first()

def get_all_utilizadores_cargos():
    return UtilizadoresCargos.objects.all()

def get_utilizadores_cargos_by_id_utilizador(id_utilizador):
    return UtilizadoresCargos.objects.filter(id=id_utilizador)

def get_utilizadores_cargos_by_id_cargo(id_cargo):
    return UtilizadoresCargos.objects.filter(id_cargo=id_cargo)