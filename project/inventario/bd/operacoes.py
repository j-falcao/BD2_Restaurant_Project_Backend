from project.utils.db_utils import fetch_from_view
from django.db import connection
from ..models import *

# Ingredientes


def create_ingredientes(ingrediente):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL create_ingredientes(%s, %s, %s, %s, %s, %s, %s, %s)', [
            ingrediente['id_fornecedor'],
            ingrediente['nome'],
            ingrediente['url_imagem'],
            ingrediente['quantidade_stock'],
            ingrediente['unidade_medida'],
            ingrediente['limite_stock'],
            ingrediente['preco'],
            None
        ])
        return cursor.fetchone()[0]


def update_ingredientes(id_ingrediente, ingrediente):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL update_ingredientes(%s, %s, %s, %s, %s, %s, %s, %s, %s)', [
            id_ingrediente,
            ingrediente['id_fornecedor'],
            ingrediente['nome'],
            ingrediente['url_imagem'],
            ingrediente['quantidade_stock'],
            ingrediente['unidade_medida'],
            ingrediente['limite_stock'],
            ingrediente['preco'],
            None
        ])
        return cursor.fetchone()[0]


def delete_ingredientes(id_ingrediente):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_ingredientes(%s)', [id_ingrediente])


# Utensílios
def create_utensilios(utensilio):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL create_utensilios(%s, %s, %s, %s, %s, %s, %s, %s)', [
            utensilio['id_fornecedor'],
            utensilio['nome'],
            utensilio['url_imagem'],
            utensilio['quantidade_stock'],
            utensilio['unidade_medida'],
            utensilio['limite_stock'],
            utensilio['preco'],
            None
        ])
        return cursor.fetchone()[0]


def update_utensilios(id_utensilio, utensilio):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL update_utensilios(%s, %s, %s, %s, %s, %s, %s, %s, %s)', [
            id_utensilio,
            utensilio['id_fornecedor'],
            utensilio['nome'],
            utensilio['url_imagem'],
            utensilio['quantidade_stock'],
            utensilio['unidade_medida'],
            utensilio['limite_stock'],
            utensilio['preco'],
            None
        ])
        return cursor.fetchone()[0]


def delete_utensilios(id_utensilio):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_utensilios(%s)', [id_utensilio])


# Fornecedores
def create_fornecedores(fornecedor):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL create_fornecedores(%s, %s, %s, %s, %s, %s, %s)', [
            fornecedor['nome'],
            fornecedor['vende_ingredientes'],
            fornecedor['vende_utensilios'],
            fornecedor['morada'],
            fornecedor['email'],
            fornecedor['telemovel'],
            None
        ])
        return cursor.fetchone()[0]


def update_fornecedores(id_fornecedor, fornecedor):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL update_fornecedores(%s, %s, %s, %s, %s, %s, %s, %s)', [
            id_fornecedor,
            fornecedor['nome'],
            fornecedor['vende_ingredientes'],
            fornecedor['vende_utensilios'],
            fornecedor['morada'],
            fornecedor['email'],
            fornecedor['telemovel'],
            None
        ])
        return cursor.fetchone()[0]


def delete_fornecedores(id_fornecedor):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_fornecedores(%s)', [id_fornecedor])


# Carrinhos - CREATE E DELETE são feitos automaticamente através de triggers
def comprar_carrinho_atual_ingredientes():  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL comprar_carrinho_atual_ingredientes(%s)', [None])
        return cursor.fetchone()[0]

def comprar_carrinho_atual_utensilios():  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL comprar_carrinho_atual_utensilios(%s)', [None])
        return cursor.fetchone()[0]


# IngredientesCarrinhos
def create_ingredientesCarrinhos_atual(data):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL create_ingredientescarrinhos_atual(%s, %s, %s, %s)', [
            data['id_ingrediente'],
            data['id_administrador'],
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def update_ingredientesCarrinhos_atual(id_ingrediente_carrinho, data):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL update_ingredientescarrinhos_atual(%s, %s, %s)', [
            id_ingrediente_carrinho,
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def delete_ingredientesCarrinhos_atual(id_ingrediente_carrinho):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_ingredientescarrinhos_atual(%s)', [
                       id_ingrediente_carrinho])


# UtensiliosCarrinhos
def create_utensiliosCarrinhos_atual(data):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL create_utensilioscarrinhos_atual(%s, %s, %s, %s)', [
            data['id_utensilio'],
            data['id_administrador'],
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def update_utensiliosCarrinhos_atual(id_utensilio_carrinho, data):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL update_utensilioscarrinhos_atual(%s, %s, %s)', [
            id_utensilio_carrinho,
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def delete_utensiliosCarrinhos_atual(id_utensilio_carrinho):  # ✅
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_utensilioscarrinhos_atual(%s)', [
                       id_utensilio_carrinho])


# Instrucoes
def create_instrucoes(id_receita, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_instrucoes(%s, %s, %s)', [
            id_receita,
            data['descricao'],
            None
        ])
        return cursor.fetchone()[0]


def update_instrucoes(id_instrucao, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_instrucoes(%s, %s, %s, %s)', [
            id_instrucao,
            data['numero_sequencia'],
            data['descricao'],
            None
        ])
        return cursor.fetchone()[0]


def delete_instrucoes(id_instrucao):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_instrucoes(%s)', [id_instrucao])


# Receitas
def create_receitas(receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_receitas(%s, %s, %s)', [
            receita['nome'],
            receita['duracao'],
            None
        ])
        return cursor.fetchone()[0]


def update_receitas(id_receita, receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_receitas(%s, %s, %s, %s)', [
            id_receita,
            receita['nome'],
            receita['duracao'],
            None
        ])
        return cursor.fetchone()[0]


def delete_receitas(id_receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_receitas(%s)', [id_receita])


# IngredientesReceitas
def create_ingredientesReceitas(id_receita, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_ingredientesreceitas(%s, %s, %s, %s)', [
            id_receita,
            data['id_ingrediente'],
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def update_ingredientesReceitas(id_ingrediente_receita, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_ingredientesreceitas(%s, %s, %s)', [
            id_ingrediente_receita,
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def delete_ingredientesReceitas(id_ingrediente_receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_ingredientesreceitas(%s)',
                       [id_ingrediente_receita])


# UtensiliosReceitas
def create_utensiliosReceitas(id_receita, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_utensiliosreceitas(%s, %s, %s, %s)', [
            id_receita,
            data['id_utensilio'],
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def update_utensiliosReceitas(id_utensilio_receita, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_utensiliosreceitas(%s, %s, %s)', [
            id_utensilio_receita,
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]


def delete_utensiliosReceitas(id_utensilio_receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_utensiliosreceitas(%s)',
                       [id_utensilio_receita])
