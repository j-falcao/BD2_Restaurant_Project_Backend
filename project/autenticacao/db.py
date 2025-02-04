from .models import *
from django.db import connection

def create_utilizador(validated_data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_utilizadores(%s, %s, %s, %s, %s, %s, %s, %s)', [
            validated_data['username'],
            validated_data['id_cargo'],
            validated_data['first_name'],
            validated_data['last_name'],
            validated_data['is_superuser'],
            validated_data['url_imagem'],
            validated_data['password'],
            None
        ])
        return cursor.fetchone()[0]

def update_utilizador(id_utilizador, validated_data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_utilizadores(%s, %s, %s, %s, %s, %s, %s, %s, %s)', [ 
            id_utilizador,
            validated_data['username'],
            validated_data['id_cargo'],
            validated_data['first_name'],
            validated_data['last_name'],
            validated_data['is_superuser'],
            validated_data['url_imagem'],
            validated_data['password'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_utilizador(id_utilizador):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_utilizadores(%s)', [id_utilizador])


""" def get_all_utilizadores():
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
    return UtilizadoresCargos.objects.filter(id_cargo=id_cargo) """