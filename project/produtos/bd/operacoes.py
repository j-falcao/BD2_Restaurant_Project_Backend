from ..models import *
from django.db import connection


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
        cursor.execute('CALL create_receitas(%s, %s, %s, %s)', [
            receita['nome'],
            receita['duracao'],
            receita['id_produto'],
            None
        ])
        return cursor.fetchone()[0]


def update_receitas(id_receita, receita):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_receitas(%s, %s, %s, %s, %s)', [
            id_receita,
            receita['nome'],
            receita['duracao'],
            receita['id_produto'],
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


# Categorias
def create_categorias(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_categorias(%s, %s)', [
            data['designacao'],
            None
        ])
        return cursor.fetchone()[0]

def update_categorias(id_categoria, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_categorias(%s, %s, %s)', [
            id_categoria,
            data['designacao'],
            None
        ])
        return cursor.fetchone()[0]

def delete_categorias(id_categoria):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_categorias(%s)', [id_categoria])


# Tipos
def create_tipos(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_tipos(%s, %s)', [
            data['designacao'],
            None
        ])
        return cursor.fetchone()[0]

def update_tipos(id_tipo, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_tipos(%s, %s, %s)', [
            id_tipo,
            data['designacao'],
            None
        ])
        return cursor.fetchone()[0]

def delete_tipos(id_tipo):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_tipos(%s)', [id_tipo])


# Opções
def create_opcoes(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_opcoes(%s, %s)', [
            data['designacao'],
            None
        ])
        return cursor.fetchone()[0]
    
def update_opcoes(id_opcao, data):
    with connection.cursor() as cursor:    
        cursor.execute('CALL update_opcoes(%s, %s, %s)', [
            id_opcao,
            data['designacao'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_opcoes(id_opcao):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_opcoes(%s)', [id_opcao])


# Itens
def create_item(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itens(%s, %s, %s, %s, %s, %s)', [
            data['nome'],
            data['url_imagem'],
            data['preco'],
            data['porcao_unidade_medida'],
            data['porcao'],
            None
        ])
        return cursor.fetchone()[0]
    
def update_item(id_item, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_itens(%s, %s, %s, %s, %s, %s, %s)', [
            id_item,
            data['nome'],
            data['url_imagem'],    
            data['preco'],
            data['porcao_unidade_medida'],
            data['porcao'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_item(id_item):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itens(%s)', [id_item])


# Itens Opções
def create_itensOpcoes(id_item, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itensopcoes(%s, %s, %s)', [
            id_item,
            data['id_opcao'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_itensOpcoes(id_item_opcao):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itensopcoes(%s)', [id_item_opcao])


# Itens Categorias
def create_itensCategorias(id_item, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itenscategorias(%s, %s, %s)', [
            id_item,
            data['id_categoria'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_itensCategorias(id_item_categoria):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itenscategorias(%s)', [id_item_categoria])


# Itens Tipos
def create_itensTipos(id_item, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itenstipos(%s, %s, %s)', [
            id_item,
            data['id_tipo'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_itensTipos(id_item_tipo):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itenstipos(%s)', [id_item_tipo])


# Menus
def create_menus(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_menus(%s, %s, %s, %s)', [
            data['nome'],
            data['url_imagem'],    
            data['preco'],
            None
        ])
        return cursor.fetchone()[0]
    
def update_menus(id_menu, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_menus(%s, %s, %s, %s, %s)', [
            id_menu,
            data['nome'],
            data['url_imagem'],    
            data['preco'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_menus(id_menu):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_menus(%s)', [id_menu])


# Itens Menus
def create_itensMenus(id_menu, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itensmenus(%s, %s, %s)', [
            id_menu,
            data['id_item'],
            None
        ])
        return cursor.fetchone()[0]
    
def delete_itensMenus(id_item_menu):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itensmenus(%s)', [id_item_menu])


# Menus DiasSemana
def create_menusDiasSemana(id_menu, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_menusdiassemana(%s, %s, %s, %s, %s)', [
            id_menu,
            data['id_dia_semana'],
            data['almoco'],
            data['jantar'],
            None
        ])
        return cursor.fetchone()[0]
    
def update_menusDiasSemana(id_menu_dia_semana, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_menusdiassemana(%s, %s, %s, %s)', [
            id_menu_dia_semana,
            data['almoco'],
            data['jantar'],
            None
        ])
        return cursor.fetchone()[0]

def delete_menusDiasSemana(id_menu_dia_semana):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_menusdiassemana(%s)', [id_menu_dia_semana])