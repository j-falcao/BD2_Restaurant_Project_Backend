from models import *

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
    return Utilizadores.objects.filter(permissoes__id_permissao=1)

def get_all_garcons():
    return Utilizadores.objects.filter(permissoes__id_permissao=2)

def get_all_administradores():
    return Utilizadores.objects.filter(permissoes__id_permissao=3)

def get_all_cargos():
    return Cargos.objects.all()

def get_cargo_by_id(id_cargo):
    return Cargos.objects.filter(id_cargo=id_cargo).first()

def get_cargo_by_designacao(designacao):
    return Cargos.objects.filter(designacao=designacao).first()

def get_all_permissoes():
    return Permissoes.objects.all() 

def get_permissao_by_id(id_permissao):
    return Permissoes.objects.filter(id_permissao=id_permissao).first()

def get_permissao_by_designacao(designacao):
    return Permissoes.objects.filter(designacao=designacao).first()

def get_all_utilizadores_permissoes():
    return UtilizadoresPermissoes.objects.all()

def get_utilizadores_permissoes_by_id_utilizador(id_utilizador):
    return UtilizadoresPermissoes.objects.filter(id_utilizador=id_utilizador)

def get_utilizadores_permissoes_by_id_permissao(id_permissao):
    return UtilizadoresPermissoes.objects.filter(id_permissao=id_permissao)

def get_all_utilizadores_cargos():
    return UtilizadoresCargos.objects.all()

def get_utilizadores_cargos_by_id_utilizador(id_utilizador):
    return UtilizadoresCargos.objects.filter(id_utilizador=id_utilizador)

def get_utilizadores_cargos_by_id_cargo(id_cargo):
    return UtilizadoresCargos.objects.filter(id_cargo=id_cargo)

def get_all_permissoes_cargos():
    return PermissoesCargos.objects.all()

def get_permissoes_cargos_by_id_permissao(id_permissao):
    return PermissoesCargos.objects.filter(id_permissao=id_permissao)

def get_permissoes_cargos_by_id_cargo(id_cargo):
    return PermissoesCargos.objects.filter(id_cargo=id_cargo)