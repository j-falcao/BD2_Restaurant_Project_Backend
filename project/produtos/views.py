from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import db
from .models import *

@api_view(['GET', 'POST'])
def get_post_tipos(request):
    if request.method == 'GET':
        return Response(Tipos.fetch_all())
    elif request.method == 'POST':
        return Response(db.create_tipos(request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
def update_delete_tipos(request, id_tipo):
    if request.method == 'PUT':
        return Response(db.update_tipos(id_tipo, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_tipos(id_tipo)        
        return Response({"msg": "Tipo apagado"}, status=200)
    
@api_view(['GET', 'POST'])
def get_post_categorias(request):
    if request.method == 'GET':
        return Response(Categorias.fetch_all())
    elif request.method == 'POST':
        return Response(db.create_categorias(request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
def update_delete_categorias(request, id_categoria):
    if request.method == 'PUT':
        return Response(db.update_categorias(id_categoria, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_categorias(id_categoria)
        return Response({"msg": "Categoria apagada"}, status=200)

@api_view(['GET', 'POST'])
def get_post_opcoes(request):
    if request.method == 'GET':
        return Response(Opcoes.fetch_all())
    elif request.method == 'POST':
        return Response(db.create_opcoes(request.data), status=201)  
    
@api_view(['PUT', 'DELETE'])
def update_delete_opcoes(request, id_opcao):
    if request.method == 'PUT':
        return Response(db.update_opcoes(id_opcao, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_opcoes(id_opcao)
        return Response({"msg": "Opcao apagada"}, status=200)
    

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
        return Response(db.create_item(request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
def update_delete_itens(request, id_item):
    if request.method == 'PUT':
        return Response(db.update_item(id_item, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_item(id_item)
        return Response({"msg": "Item apagado"}, status=200)

@api_view(['GET', 'POST'])
def get_post_itensOpcoes(request, id_item):
    if request.method == 'GET':
        return Response(ItensOpcoes.fetch_by_item(id_item))
    elif request.method == 'POST':
        return Response(db.create_itensOpcoes(id_item, request.data), status=201)
    
@api_view(['DELETE'])
def delete_itensOpcoes(request, id_item_opcao):
    db.delete_itensOpcoes(id_item_opcao)
    return Response({"msg": "ItemOpcao apagado"}, status=200)

@api_view(['GET', 'POST'])
def get_post_itensCategorias(request, id_item):
    if request.method == 'GET':
        return Response(ItensCategorias.fetch_by_item(id_item))
    elif request.method == 'POST':
        return Response(db.create_itensCategorias(id_item, request.data), status=201)
    
@api_view(['DELETE'])
def delete_itensCategorias(request, id_item_categoria):
    db.delete_itensCategorias(id_item_categoria)
    return Response({"msg": "ItemCategoria apagado"}, status=200)

@api_view(['GET', 'POST'])
def get_post_itensTipos(request, id_item):
    if request.method == 'GET':
        return Response(ItensTipos.fetch_by_item(id_item))
    elif request.method == 'POST':
        return Response(db.create_itensTipos(id_item, request.data), status=201)
    
@api_view(['DELETE'])
def delete_itensTipos(request, id_item_tipo):
    db.delete_itensTipos(id_item_tipo)
    return Response({"msg": "ItemTipo apagado"}, status=200)

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
        return Response(db.create_menus(request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
def update_delete_menus(request, id_menu):
    if request.method == 'PUT':
        return Response(db.update_menus(id_menu, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_menus(id_menu)
        return Response({"msg": "Menu apagado"}, status=200)
    
@api_view(['GET', 'POST'])
def get_post_itensMenus(request, id_menu):
    if request.method == 'GET':
        return Response(ItensMenus.fetch_by_menu(id_menu))
    elif request.method == 'POST':
        return Response(db.create_itensMenus(id_menu, request.data), status=201)
    
@api_view(['DELETE'])
def update_delete_itensMenus(request, id_item_menu):
    db.delete_itensMenus(id_item_menu)
    return Response({"msg": "ItemMenu apagado"}, status=200)


@api_view(['GET', 'POST'])
def get_post_menusDiasSemana(request, id_menu):
    if request.method == 'GET':
        return Response(MenusDiasSemana.fetch_by_menu(id_menu))
    elif request.method == 'POST':
        return Response(db.create_menusDiasSemana(id_menu, request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
def update_delete_menusDiasSemana(request, id_menu_dia_semana):
    if request.method == 'PUT':
        return Response(db.update_menusDiasSemana(id_menu_dia_semana, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_menusDiasSemana(id_menu_dia_semana)
        return Response({"msg": "MenuDiaSemana apagado"}, status=200)

@api_view(['GET'])
def get_menus_by_dia_semana(request, id_dia_semana):
    return Response(MenusDiasSemana.fetch_by_dia_semana(id_dia_semana))