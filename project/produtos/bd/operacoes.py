from ..models import *
from django.db import connection
from estatisticas import operacoes_recolha as estatisticas


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
        cursor.execute('CALL delete_utensiliosreceitas(%s)', [id_utensilio_receita])


# Categorias
def create_categorias(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_categorias(%s, %s)', [
            data['designacao'],
            None
        ])
        categoria = cursor.fetchone()[0]
        estatisticas.create_categoria({**categoria})
        return categoria

def update_categorias(id_categoria, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_categorias(%s, %s, %s)', [
            id_categoria,
            data['designacao'],
            None
        ])
        categoria = cursor.fetchone()[0]
        estatisticas.update_categoria({**categoria})
        return categoria

def delete_categorias(id_categoria):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_categorias(%s)', [id_categoria])
        estatisticas.delete_categoria(id_categoria)


# Tipos
def create_tipos(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_tipos(%s, %s)', [
            data['designacao'],
            None
        ])
        tipo = cursor.fetchone()[0]
        estatisticas.create_tipo({**tipo})
        return tipo

def update_tipos(id_tipo, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_tipos(%s, %s, %s)', [
            id_tipo,
            data['designacao'],
            None
        ])
        tipo = cursor.fetchone()[0]
        estatisticas.update_tipo({**tipo})
        return tipo

def delete_tipos(id_tipo):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_tipos(%s)', [id_tipo])
        estatisticas.delete_tipo(id_tipo)


# Opções
def create_opcoes(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_opcoes(%s, %s)', [
            data['designacao'],
            None
        ])
        opcao = cursor.fetchone()[0]
        estatisticas.create_opcao({**opcao})
        return opcao
    
def update_opcoes(id_opcao, data):
    with connection.cursor() as cursor:    
        cursor.execute('CALL update_opcoes(%s, %s, %s)', [
            id_opcao,
            data['designacao'],
            None
        ])
        opcao = cursor.fetchone()[0]
        estatisticas.update_opcao({**opcao})
        return opcao
    
def delete_opcoes(id_opcao):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_opcoes(%s)', [id_opcao])
        estatisticas.delete_opcao(id_opcao)


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
        item = cursor.fetchone()[0]
        estatisticas.create_item({**item})
        return item
    
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
        item = cursor.fetchone()[0]
        estatisticas.update_item({**item})
        return item
    
def delete_item(id_item):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itens(%s, %s)', [id_item, None])
        estatisticas.delete_item(cursor.fetchone()[0])


# Itens Opções
def create_itensOpcoes(id_item, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itensopcoes(%s, %s, %s)', [
            id_item,
            data['id_opcao'],
            None
        ])
        itemopcao = cursor.fetchone()[0]
        estatisticas.create_itemopcao({**itemopcao})
        return itemopcao
    
def delete_itensOpcoes(id_item_opcao):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itensopcoes(%s, %s)', [id_item_opcao, None])
        estatisticas.delete_itemopcao(cursor.fetchone()[0])


# Itens Categorias
def create_itensCategorias(id_item, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itenscategorias(%s, %s, %s)', [
            id_item,
            data['id_categoria'],
            None
        ])
        itemcategoria = cursor.fetchone()[0]
        estatisticas.create_itemcategoria({**itemcategoria})
        return itemcategoria
    
def delete_itensCategorias(id_item_categoria):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itenscategorias(%s, %s)', [id_item_categoria, None])
        estatisticas.delete_itemcategoria(cursor.fetchone()[0])


# Itens Tipos
def create_itensTipos(id_item, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_itenstipos(%s, %s, %s)', [
            id_item,
            data['id_tipo'],
            None
        ])
        itemtipo = cursor.fetchone()[0]
        estatisticas.create_itemtipo({**itemtipo})
        return itemtipo
    
def delete_itensTipos(id_item_tipo):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itenstipos(%s, %s)', [id_item_tipo, None])
        estatisticas.delete_itemtipo(cursor.fetchone()[0])

# Menus
def create_menus(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_menus(%s, %s, %s, %s)', [
            data['nome'],
            data['url_imagem'],    
            data['preco'],
            None
        ])
        menu = cursor.fetchone()[0]
        estatisticas.create_menu({**menu})
        return menu
    
def update_menus(id_menu, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_menus(%s, %s, %s, %s, %s)', [
            id_menu,
            data['nome'],
            data['url_imagem'],    
            data['preco'],
            None
        ])
        menu = cursor.fetchone()[0]
        estatisticas.update_menu({**menu})
        return menu
    
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
        itemmenu = cursor.fetchone()[0]
        estatisticas.create_itemmenu({**itemmenu})
        return itemmenu
    
def delete_itensMenus(id_item_menu):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_itensmenus(%s, %s)', [id_item_menu, None])
        estatisticas.delete_itemmenu(cursor.fetchone()[0])


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