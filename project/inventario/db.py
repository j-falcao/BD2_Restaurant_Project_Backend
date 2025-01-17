from django.db import connection
from .models import *

# Ingredientes
def get_ingredientes(id_ingrediente=None):
    if id_ingrediente:
        return Ingredientes.objects.get(id_ingrediente=id_ingrediente)
    return Ingredientes.objects.all()

def create_ingredientes(ingrediente):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_ingredientes(%s, %s, %s, %s, %s, %s, %s)', [
            ingrediente['id_fornecedor'],
            ingrediente['nome'],
            ingrediente['url_imagem'],
            ingrediente['quantidade_stock'],
            ingrediente['unidade_medida'],
            ingrediente['limite_stock'],
            ingrediente['preco']
        ])

def update_ingredientes(id_ingrediente, ingrediente):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_ingredientes(%s, %s, %s, %s, %s, %s, %s, %s)', [
            id_ingrediente,
            ingrediente['id_fornecedor'],
            ingrediente['nome'],
            ingrediente['url_imagem'],
            ingrediente['quantidade_stock'],
            ingrediente['unidade_medida'],
            ingrediente['limite_stock'],
            ingrediente['preco']
        ])

def delete_ingredientes(id_ingrediente):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_ingredientes(%s)', [id_ingrediente])


# Utensílios
def get_utensilios(id_utensilio=None):
    if id_utensilio:
        return Utensilios.objects.get(id_utensilio=id_utensilio)
    return Utensilios.objects.all()

def create_utensilios(utensilio):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_utensilios(%s, %s)', [
            utensilio['nome'],
            utensilio['url_imagem'],
            utensilio['quantidade_stock'],
            utensilio['limite_stock'],
            utensilio['preco'],
            utensilio['id_fornecedor']
        ])

def update_utensilios(id_utensilio, utensilio):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_utensilios(%s, %s, %s)', [
            id_utensilio,
            utensilio['nome'],
            utensilio['url_imagem'],
            utensilio['quantidade_stock'],
            utensilio['limite_stock'],
            utensilio['preco'],
            utensilio['id_fornecedor']
        ])

def delete_utensilios(id_utensilio):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_utensilios(%s)', [id_utensilio])


# Fornecedores
def get_fornecedores(id_fornecedor=None):
    if id_fornecedor:
        return Fornecedores.objects.get(id_fornecedor=id_fornecedor)
    return Fornecedores.objects.all()

def create_fornecedors(fornecedor):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_fornecedor(%s, %s, %s, %s, %s, %s)', [
            fornecedor['nome'],
            fornecedor['vende_ingredientes'],
            fornecedor['vende_utensilios'],
            fornecedor['morada'],
            fornecedor['email'],
            fornecedor['telefone']
        ])

def update_fornecedors(id_fornecedor, fornecedor):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_fornecedor(%s, %s, %s, %s, %s, %s, %s)', [
            id_fornecedor,
            fornecedor['nome'],
            fornecedor['vende_ingredientes'],
            fornecedor['vende_utensilios'],
            fornecedor['morada'],
            fornecedor['email'],
            fornecedor['telefone']
        ])

def delete_fornecedors(id_fornecedor):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_fornecedor(%s)', [id_fornecedor])


# Carrinhos
def get_carrinhos(id_carrinho=None):
    if id_carrinho:
        return Carrinhos.objects.get(id_carrinho=id_carrinho)
    return Carrinhos.objects.all()

def create_carrinhos(carrinho):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_carrinho(%s, %s)', [
            carrinho['preco_total'],
            carrinho['data_compra']
        ])

def update_carrinhos(id_carrinho, carrinho):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_carrinho(%s, %s, %s)', [
            id_carrinho,
            carrinho['preco_total'],
            carrinho['data_compra']
        ])

def delete_carrinhos(id_carrinho):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_carrinho(%s)', [id_carrinho])


# IngredientesCarrinhos
def get_ingredientesCarrinhos(id_ingrediente_administrador=None):
    if id_ingrediente_administrador:
        return IngredientesCarrinhos.objects.get(id_ingrediente_administrador=id_ingrediente_administrador)
    return IngredientesCarrinhos.objects.all()

def create_ingredientesCarrinhos(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_ingrediente_carrinho(%s, %s, %s, %s)', [
            data['id_ingrediente'],
            data['id_administrador'],
            data['id_carrinho'],
            data['quantidade']
        ])

def update_ingredientesCarrinhos(id_ingrediente_administrador, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_ingrediente_carrinho(%s, %s, %s, %s, %s)', [
            id_ingrediente_administrador,
            data['id_ingrediente'],
            data['id_administrador'],
            data['id_carrinho'],
            data['quantidade']
        ])

def delete_ingredientesCarrinhos(id_ingrediente_administrador):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_ingrediente_carrinho(%s)', [id_ingrediente_administrador])


# UtensiliosCarrinhos
def get_utensiliosCarrinhos(id_utensilio_carrinho=None):
    if id_utensilio_carrinho:
        return UtensiliosCarrinhos.objects.get(id_utensilio_carrinho=id_utensilio_carrinho)
    return UtensiliosCarrinhos.objects.all()

def create_utensiliosCarrinhos(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_utensilio_carrinho(%s, %s, %s, %s)', [
            data['id_utensilio'],
            data['id_administrador'],
            data['id_carrinho'],
            data['quantidade']
        ])

def update_utensiliosCarrinhos(id_utensilio_carrinho, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_utensilio_carrinho(%s, %s, %s, %s, %s)', [
            id_utensilio_carrinho,
            data['id_utensilio'],
            data['id_administrador'],
            data['id_carrinho'],
            data['quantidade']
        ])

def delete_utensiliosCarrinhos(id_utensilio_carrinho):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_utensilio_carrinho(%s)', [id_utensilio_carrinho])


# Instrucoes
def get_instrucoes(id_instrucao=None):
    if id_instrucao:
        return Instrucoes.objects.get(id_instrucao=id_instrucao)
    return Instrucoes.objects.all()

def create_instrucoes(instrucao):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_instrucao(%s, %s, %s)', [
            instrucao['numero_sequencia'],
            instrucao['id_receita'],
            instrucao['descricao']
        ])

def update_instrucoes(id_instrucao, instrucao):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_instrucao(%s, %s, %s, %s)', [
            id_instrucao,
            instrucao['numero_sequencia'],
            instrucao['id_receita'],
            instrucao['descricao']
        ])

def delete_instrucoes(id_instrucao):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_instrucao(%s)', [id_instrucao])


# Receitas
def get_receitas(id_receita=None):
    if id_receita:
        return Receitas.objects.get(id_receita=id_receita)
    return Receitas.objects.all()

def create_receitas(receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_receita(%s, %s)', [
            receita['nome'],
            receita['duracao']
        ])

def update_receitas(id_receita, receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_receita(%s, %s, %s)', [
            id_receita,
            receita['nome'],
            receita['duracao']
        ])

def delete_receitas(id_receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_receita(%s)', [id_receita])


# UtensiliosReceitas
def get_utensiliosReceitas(id_utensilio_receita=None):
    if id_utensilio_receita:
        return UtensiliosReceitas.objects.get(id_utensilio_receita=id_utensilio_receita)
    return UtensiliosReceitas.objects.all()

def create_utensiliosReceitas(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_utensilio_receita(%s, %s)', [
            data['id_utensilio'],
            data['id_receita']
        ])

def update_utensiliosReceitas(id_utensilio_receita, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_utensilio_receita(%s, %s, %s)', [
            id_utensilio_receita,
            data['id_utensilio'],
            data['id_receita']
        ])

def delete_utensiliosReceitas(id_utensilio_receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_utensilio_receita(%s)', [id_utensilio_receita])


# IngredientesReceitas
def get_ingredientesReceitas(id_ingrediente_receita=None):
    if id_ingrediente_receita:
        return IngredientesReceitas.objects.get(id_ingrediente_receita=id_ingrediente_receita)
    return IngredientesReceitas.objects.all()

def create_ingredientesReceitas(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_ingrediente_receita(%s, %s)', [
            data['id_ingrediente'],
            data['id_receita']
        ])

def update_ingredientesReceitas(id_ingrediente_receita, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_ingrediente_receita(%s, %s, %s)', [
            id_ingrediente_receita,
            data['id_ingrediente'],
            data['id_receita']
        ])

def delete_ingredientesReceitas(id_ingrediente_receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_ingrediente_receita(%s)', [id_ingrediente_receita])

