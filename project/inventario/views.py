from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from .bd import operacoes

# Ingredientes


@api_view(['GET', 'POST'])
def get_post_ingredientes(request):  # ✅
    if request.method == 'GET':
        id_ingrediente = request.GET.get('id_ingrediente')
        if id_ingrediente:
            try:
                return Response(Ingredientes.fetch_by_id(id_ingrediente))
            except Ingredientes.DoesNotExist:
                raise NotFound("Ingrediente não encontrado")
        else:
            return Response(Ingredientes.fetch_all())

    elif request.method == 'POST':
        return Response(operacoes.create_ingredientes(request.data), status=201)


@api_view(['GET'])
def get_ingredientes_by_fornecedor(request, id_fornecedor):  # ✅
    return Response(Ingredientes.fetch_by_fornecedor(id_fornecedor))


@api_view(['PUT', 'DELETE'])
def update_delete_ingredientes(request, id_ingrediente):  # ✅
    if request.method == 'PUT':
        return Response(operacoes.update_ingredientes(id_ingrediente, request.data), status=200)

    elif request.method == 'DELETE':
        operacoes.delete_ingredientes(id_ingrediente)
        return Response({"msg": "Ingrediente apagado"}, status=204)


# Utensílios ✅
@api_view(['GET', 'POST'])
def get_post_utensilios(request):  # ✅
    if request.method == 'GET':
        id_utensilio = request.GET.get('id_utensilio')
        if id_utensilio:
            try:
                return Response(Utensilios.fetch_by_id(id_utensilio))
            except Utensilios.DoesNotExist:
                raise NotFound("Utensílio não encontrado")
        else:
            return Response(Utensilios.fetch_all())

    elif request.method == 'POST':
        return Response(operacoes.create_utensilios(request.data), status=201)


@api_view(['GET'])
def get_utensilios_by_fornecedor(request, id_fornecedor):  # ✅
    return Response(Utensilios.fetch_by_fornecedor(id_fornecedor))


@api_view(['PUT', 'DELETE'])
def update_delete_utensilios(request, id_utensilio):  # ✅
    if request.method == 'PUT':
        return Response(operacoes.update_utensilios(id_utensilio, request.data), status=200)

    elif request.method == 'DELETE':
        operacoes.delete_utensilios(id_utensilio)
        return Response({"msg": "Utensílio apagado"}, status=200)


# Fornecedores
@api_view(['GET', 'POST'])
def get_post_fornecedores(request):  # ✅
    if request.method == 'GET':
        id_fornecedor = request.GET.get('id_fornecedor')
        if id_fornecedor:
            try:
                return Response(Fornecedores.fetch_by_id(id_fornecedor))
            except Fornecedores.DoesNotExist:
                raise NotFound("Fornecedor nao encontrado")
        else:
            return Response(Fornecedores.fetch_all())

    elif request.method == 'POST':
        return Response(operacoes.create_fornecedores(request.data), status=201)


@api_view(['PUT', 'DELETE'])
def update_delete_fornecedores(request, id_fornecedor):  # ✅
    if request.method == 'PUT':
        return Response(operacoes.update_fornecedores(id_fornecedor, request.data), status=200)

    elif request.method == 'DELETE':
        operacoes.delete_fornecedores(id_fornecedor)
        return Response({"msg": "Fornecedor apagado"}, status=200)


# Carrinhos
@api_view(['GET'])
def get_carrinhos(request):
    if request.method == 'GET':
        id_carrinho = request.GET.get('id_carrinho')
        if id_carrinho:
            try:
                return Response(Carrinhos.fetch_by_id(id_carrinho))
            except Carrinhos.DoesNotExist:
                raise NotFound("Carrinho não encontrado")
        else:
            return Response(Carrinhos.fetch_all())

@api_view(['GET'])
def get_carrinho_atual(request):
    tipo = request.GET.get('tipo_carrinho')
    if not tipo:
        raise NotFound("Especifique o tipo_carrinho ('Ingredientes' ou 'Utensilios')")
    
    if tipo == 'Ingredientes':
        return Response(Carrinhos.fetch_atual_ingredientes())
    elif tipo == 'Utensilios':
        return Response(Carrinhos.fetch_atual_utensilios())
    

@api_view(['POST'])
def comprar_carrinho_atual_ingredientes(request):
    return Response(operacoes.comprar_carrinho_atual_ingredientes(), status=200)

@api_view(['POST'])
def comprar_carrinho_atual_utensilios(request):
    return Response(operacoes.comprar_carrinho_atual_utensilios(), status=200)


# IngredientesCarrinhos
@api_view(['GET', 'POST'])
def get_post_ingredientesCarrinhos_atual(request):
    if request.method == 'GET':
        return Response(IngredientesCarrinhos.fetch_by_carrinho_atual())
    elif request.method == 'POST':
        return Response(operacoes.create_ingredientesCarrinhos_atual(request.data), status=201)


@api_view(['GET'])
def get_ingredientesCarrinhos(request, id_carrinho):
    return Response(IngredientesCarrinhos.fetch_by_carrinho(id_carrinho))


@api_view(['PUT', 'DELETE'])
def update_delete_ingredientesCarrinhos_atual(request, id_ingrediente_carrinho):
    if request.method == 'PUT':
        return Response(operacoes.update_ingredientesCarrinhos_atual(id_ingrediente_carrinho, request.data))
    elif request.method == 'DELETE':
        operacoes.delete_ingredientesCarrinhos_atual(id_ingrediente_carrinho)
        return Response({"msg": "IngredienteCarrinho apagado"}, status=200)


# UtensiliosCarrinhos
@api_view(['GET', 'POST'])
def get_post_utensiliosCarrinhos_atual(request):
    if request.method == 'GET':
        return Response(UtensiliosCarrinhos.fetch_by_carrinho_atual())
    elif request.method == 'POST':
        return Response(operacoes.create_utensiliosCarrinhos_atual(request.data), status=201)


@api_view(['GET'])
def get_utensiliosCarrinhos(request, id_carrinho):
    return Response(UtensiliosCarrinhos.fetch_by_carrinho(id_carrinho))


@api_view(['PUT', 'DELETE'])
def update_delete_utensiliosCarrinhos_atual(request, id_utensilio_carrinho):
    if request.method == 'PUT':
        return Response(operacoes.update_utensiliosCarrinhos_atual(id_utensilio_carrinho, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_utensiliosCarrinhos_atual(id_utensilio_carrinho)
        return Response({"msg": "UtensilioCarrinho apagado"}, status=200)