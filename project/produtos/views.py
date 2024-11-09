from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import *
from . import db_produtos as db

@api_view(['GET'])
def get_produtos(request):
    produtos = db.get_all_produtos()
    serializer = ProdutoSerializer(produtos, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_produto(request, id_produto):
    produto = db.get_produto_by_id(id_produto)
    serializer = ProdutoSerializer(produto)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_itens(request):
    itens = db.get_all_itens()
    serializer = ItemSerializer(itens, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_item(request, id_item):
    item = db.get_item_by_id(id_item)
    serializer = ItemSerializer(item)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_tipos(request):
    tipos = db.get_all_tipos()
    serializer = TipoSerializer(tipos, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_tipo(request, id_tipo):
    tipo = db.get_tipo_by_id(id_tipo)
    serializer = TipoSerializer(tipo)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_categorias(request):
    categorias = db.get_all_categorias()
    serializer = CategoriaSerializer(categorias, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_categoria(request, id_categoria):
    categoria = db.get_categoria_by_id(id_categoria)
    serializer = CategoriaSerializer(categoria)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_opcoes(request):
    opcoes = db.get_all_opcoes()
    serializer = OpcaoSerializer(opcoes, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_opcao(request, id_opcao):
    opcao = db.get_opcao_by_id(id_opcao)
    serializer = OpcaoSerializer(opcao)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_menus(request):
    menus = db.get_all_menus()
    serializer = MenuSerializer(menus, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_menu(request, id_menu):
    menu = db.get_menu_by_id(id_menu)
    serializer = MenuSerializer(menu)
    return JsonResponse(serializer.data, safe=False)
