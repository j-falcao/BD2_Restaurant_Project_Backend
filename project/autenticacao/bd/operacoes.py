from ..models import *
from django.db import connection
from estatisticas import operacoes_recolha as estatisticas

def mee_bd():
    with connection.cursor() as cursor:
        cursor.execute('CALL mee(%s)', [None])
        return cursor.fetchone()[0]

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