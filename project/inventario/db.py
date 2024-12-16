from django.db import connection
from .models import *


def get_all_ingredientes():
    return Ingredientes.objects.all()

def get_ingrediente_by_id(id_ingrediente):
    return Ingredientes.objects.get(id_ingrediente=id_ingrediente)

def create_ingrediente(ingrediente):
    with connection.cursor() as cursor:
        cursor.callproc('create_ingrediente', [
            ingrediente['id_fornecedor'],
            ingrediente['nome'],
            ingrediente['url_imagem'],
            ingrediente['quantidade_stock'],
            ingrediente['unidade_medida'],
            ingrediente['limite_stock'],
            ingrediente['preco']
        ])

def update_ingrediente(id_ingrediente, ingrediente):
    with connection.cursor() as cursor:
        cursor.callproc('update_ingrediente', [
            id_ingrediente,
            ingrediente['id_fornecedor'],
            ingrediente['nome'],
            ingrediente['url_imagem'],
            ingrediente['quantidade_stock'],
            ingrediente['unidade_medida'],
            ingrediente['limite_stock'],
            ingrediente['preco']
        ])

def delete_ingrediente(id_ingrediente):
    with connection.cursor() as cursor:
        cursor.callproc('delete_ingrediente', [id_ingrediente])

def get_all_utensilios():
    return Utensilios.objects.all()

def get_utensilio_by_id(id_utensilio):
    return Utensilios.objects.get(id_utensilio=id_utensilio)


def get_all_receitas():
    return Receitas.objects.all()

def get_receita_by_id(id_receita):
    return Receitas.objects.get(id_receita=id_receita)


def get_all_carrinhos():
    return Carrinhos.objects.all()

def get_carrinho_by_id(id_carrinho):
    return Carrinhos.objects.get(id_carrinho=id_carrinho)


def get_all_fornecedores():
    return Fornecedores.objects.all()

def get_fornecedor_by_id(id_fornecedor):
    return Fornecedores.objects.get(id_fornecedor=id_fornecedor)