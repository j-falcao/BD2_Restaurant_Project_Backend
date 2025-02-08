from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from .bd import operacoes
from .models import *

# TIPOS
@api_view(['GET', 'POST'])
def get_post_tipos(request):
    if request.method == 'GET':
        id_tipo = request.GET.get('id_tipo')
        if id_tipo:
            try:
                return Response(Tipos.fetch_by_id(id_tipo))
            except Tipos.DoesNotExist:
                raise NotFound("Tipo nao encontrado")
        else:
            return Response(Tipos.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_tipos(request.data), status=201)

@api_view(['GET'])
def get_itens_by_tipo(request, id_tipo):
    return Response(Itens.fetch_by_tipo(id_tipo))

@api_view(['PUT', 'DELETE'])
def update_delete_tipos(request, id_tipo):
    if request.method == 'PUT':
        return Response(operacoes.update_tipos(id_tipo, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_tipos(id_tipo)
        return Response({"msg": "Tipo apagado"}, status=200)


# CATEGORIAS
@api_view(['GET', 'POST'])
def get_post_categorias(request):
    if request.method == 'GET':
        return Response(Categorias.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_categorias(request.data), status=201)

@api_view(['GET'])
def get_itens_by_categoria(request, id_categoria):
    return Response(Itens.fetch_by_categoria(id_categoria))

@api_view(['PUT', 'DELETE'])
def update_delete_categorias(request, id_categoria):
    if request.method == 'PUT':
        return Response(operacoes.update_categorias(id_categoria, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_categorias(id_categoria)
        return Response({"msg": "Categoria apagada"}, status=200)


# OPCOES
@api_view(['GET', 'POST'])
def get_post_opcoes(request):
    if request.method == 'GET':
        return Response(Opcoes.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_opcoes(request.data), status=201)

@api_view(['GET'])
def get_itens_by_opcao(request, id_opcao):
    return Response(Itens.fetch_by_opcao(id_opcao))

@api_view(['PUT', 'DELETE'])
def update_delete_opcoes(request, id_opcao):
    if request.method == 'PUT':
        return Response(operacoes.update_opcoes(id_opcao, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_opcoes(id_opcao)
        return Response({"msg": "Opcao apagada"}, status=200)


# ITENS
@api_view(['GET', 'POST'])
def get_post_itens(request):
    if request.method == 'GET':
        id_item = request.GET.get('id_item')
        if id_item:
            try:
                return Response(Itens.fetch_by_id(id_item))
            except Itens.DoesNotExist:
                raise NotFound("Item nao encontrado")
        return Response(Itens.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_item(request.data), status=201)
    
@api_view(['GET'])
def get_itens_by_menu(request, id_menu):
    return Response(Itens.fetch_by_menu(id_menu))

@api_view(['PUT', 'DELETE'])
def update_delete_itens(request, id_item):
    if request.method == 'PUT':
        return Response(operacoes.update_item(id_item, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_item(id_item)
        return Response({"msg": "Item apagado"}, status=200)


# ITENS OPCOES
@api_view(['GET', 'POST'])
def get_post_itensOpcoes(request, id_item):
    if request.method == 'GET':
        return Response(Opcoes.fetch_by_item(id_item))
    elif request.method == 'POST':
        return Response(operacoes.create_itensOpcoes(id_item, request.data), status=201)

@api_view(['DELETE'])
def delete_itensOpcoes(request, id_item_opcao):
    operacoes.delete_itensOpcoes(id_item_opcao)
    return Response({"msg": "ItemOpcao apagado"}, status=200)


# ITENS CATEGORIAS
@api_view(['GET', 'POST'])
def get_post_itensCategorias(request, id_item):
    if request.method == 'GET':
        return Response(Categorias.fetch_by_item(id_item))
    elif request.method == 'POST':
        return Response(operacoes.create_itensCategorias(id_item, request.data), status=201)

@api_view(['DELETE'])
def delete_itensCategorias(request, id_item_categoria):
    operacoes.delete_itensCategorias(id_item_categoria)
    return Response({"msg": "ItemCategoria apagado"}, status=200)


# ITENS TIPOS
@api_view(['GET', 'POST'])
def get_post_itensTipos(request, id_item):
    if request.method == 'GET':
        return Response(Tipos.fetch_by_item(id_item))
    elif request.method == 'POST':
        return Response(operacoes.create_itensTipos(id_item, request.data), status=201)

@api_view(['DELETE'])
def delete_itensTipos(request, id_item_tipo):
    operacoes.delete_itensTipos(id_item_tipo)
    return Response({"msg": "ItemTipo apagado"}, status=200)


# MENUS
@api_view(['GET', 'POST'])
def get_post_menus(request):
    if request.method == 'GET':
        id_menu = request.GET.get('id_menu')
        if id_menu:
            try:
                return Response(Menus.fetch_by_id(id_menu))
            except Menus.DoesNotExist:
                raise NotFound("Menu nao encontrado")
        else:
            return Response(Menus.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_menus(request.data), status=201)
    
@api_view(['GET'])
def get_menus_by_diasemana(request, id_dia_semana):
    return Response(Menus.fetch_by_diasemana(id_dia_semana))

@api_view(['GET'])
def get_menus_by_item(request, id_item):
    return Response(Menus.fetch_by_item(id_item))

@api_view(['PUT', 'DELETE'])
def update_delete_menus(request, id_menu):
    if request.method == 'PUT':
        return Response(operacoes.update_menus(id_menu, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_menus(id_menu)
        return Response({"msg": "Menu apagado"}, status=200)


# ITENS MENUS
@api_view(['GET', 'POST'])
def get_post_itensMenus(request, id_menu):
    if request.method == 'GET':
        return Response(Itens.fetch_by_menu(id_menu))
    elif request.method == 'POST':
        return Response(operacoes.create_itensMenus(id_menu, request.data), status=201)

@api_view(['DELETE'])
def update_delete_itensMenus(request, id_item_menu):
    operacoes.delete_itensMenus(id_item_menu)
    return Response({"msg": "ItemMenu apagado"}, status=200)


# MENUS DIAS SEMANA
@api_view(['GET', 'POST'])
def get_post_menusDiasSemana(request, id_menu):
    if request.method == 'GET':
        return Response(DiasSemana.fetch_by_menu(id_menu))
    elif request.method == 'POST':
        return Response(operacoes.create_menusDiasSemana(id_menu, request.data), status=201)

@api_view(['PUT', 'DELETE'])
def update_delete_menusDiasSemana(request, id_menu_dia_semana):
    if request.method == 'PUT':
        return Response(operacoes.update_menusDiasSemana(id_menu_dia_semana, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_menusDiasSemana(id_menu_dia_semana)
        return Response({"msg": "MenuDiaSemana apagado"}, status=200)