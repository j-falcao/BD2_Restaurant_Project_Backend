from .models import *
from django.db import connection

def create_utilizador(validated_data):
    with connection.cursor() as cursor:
        cursor.callproc(
            'create_utilizador', 
            [
                validated_data.get('username'),
                validated_data.get('first_name'),
                validated_data.get('last_name'),
                validated_data.get('password'),
                validated_data.get('telemovel'),
                validated_data.get('data_nascimento'),
                validated_data.get('genero'),
                validated_data.get('url_imagem'),
                validated_data.get('turno_almoco'),
                validated_data.get('turno_jantar'),
            ]
        )

def get_all_utilizadores():
    return Utilizadores.objects.all()

def get_utilizador_by_username(username):
    return Utilizadores.objects.filter(username=username).first()

def get_utilizador_by_id(id_utilizador):
    return Utilizadores.objects.filter(id_utilizador=id_utilizador).first()

def get_utilizador_by_email(email):
    return Utilizadores.objects.filter(email=email).first()

def get_utilizador_by_telemovel(telemovel):
    return Utilizadores.objects.filter(telemovel=telemovel).first() 

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
    return UtilizadoresCargos.objects.filter(id_utilizador=id_utilizador)

def get_utilizadores_cargos_by_id_cargo(id_cargo):
    return UtilizadoresCargos.objects.filter(id_cargo=id_cargo)