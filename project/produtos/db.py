from .models import Produto, Item, Tipo, Categoria, Opcao, Menu

def get_all_produtos():
    return Produto.objects.all()

def get_produto_by_id(id_produto):
    return Produto.objects.get(id_produto=id_produto)


def get_all_itens():
    return Item.objects.all()

def get_item_by_id(id_item):
    return Item.objects.get(id_item=id_item)


def get_all_tipos():
    return Tipo.objects.all()

def get_tipo_by_id(id_tipo):
    return Tipo.objects.get(id_tipo=id_tipo)


def get_all_categorias():
    return Categoria.objects.all()

def get_categoria_by_id(id_categoria):
    return Categoria.objects.get(id_categoria=id_categoria)


def get_all_opcoes():
    return Opcao.objects.all()

def get_opcao_by_id(id_opcao):
    return Opcao.objects.get(id_opcao=id_opcao)


def get_all_menus():
    return Menu.objects.all()

def get_menu_by_id(id_menu):
    return Menu.objects.get(id_menu=id_menu)
