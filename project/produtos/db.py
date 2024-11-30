from .models import *

def get_all_produtos():
    return Produtos.objects.all()

def get_produto_by_id(id_produto):
    return Produtos.objects.get(id_produto=id_produto)


def get_all_itens():
    return Itens.objects.all()

def get_item_by_id(id_item):
    return Itens.objects.get(id_item=id_item)

def get_itens_by_categoria(id_categoria):
    return Itens.objects.filter(categorias=id_categoria)


def get_all_tipos():
    return Tipos.objects.all()

def get_tipo_by_id(id_tipo):
    return Tipos.objects.get(id_tipo=id_tipo)


def get_all_categorias():
    return Categorias.objects.all()

def get_categoria_by_id(id_categoria):
    return Categorias.objects.get(id_categoria=id_categoria)


def get_all_opcoes():
    return Opcoes.objects.all()

def get_opcao_by_id(id_opcao):
    return Opcoes.objects.get(id_opcao=id_opcao)


def get_all_menus():
    return Menus.objects.all()

def get_menu_by_id(id_menu):
    return Menus.objects.get(id_menu=id_menu)
