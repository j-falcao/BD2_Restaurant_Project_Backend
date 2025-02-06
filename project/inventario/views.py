from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from .bd import operacoes

# Ingredientes
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_ingredientes(request): #✅
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

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_ingredientes(request, id_ingrediente): #✅
    if request.method == 'PUT':
        return Response(operacoes.update_ingredientes(id_ingrediente, request.data), status=200)

    elif request.method == 'DELETE':
        operacoes.delete_ingredientes(id_ingrediente)
        return Response({"msg": "Ingrediente apagado"}, status=204)


# Utensílios ✅
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_utensilios(request): #✅
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

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_utensilios(request, id_utensilio): #✅
    if request.method == 'PUT':
        return Response(operacoes.update_utensilios(id_utensilio, request.data), status=200)

    elif request.method == 'DELETE':
        operacoes.delete_utensilios(id_utensilio)
        return Response({"msg": "Utensílio apagado"}, status=200)


# Fornecedores
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_fornecedores(request): #✅
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
@permission_classes([AllowAny])
def update_delete_fornecedores(request, id_fornecedor): #✅
    if request.method == 'PUT':
        return Response(operacoes.update_fornecedores(id_fornecedor, request.data), status=200)

    elif request.method == 'DELETE':
        operacoes.delete_fornecedores(id_fornecedor)
        return Response({"msg": "Fornecedor apagado"}, status=200)


# Carrinhos
@api_view(['GET'])
@permission_classes([AllowAny])
def get_carrinhos(request):
    if request.method == 'GET':
        # Carrinho por id
        id_carrinho = request.GET.get('id_carrinho')
        if id_carrinho:
            try:
                return Response(Carrinhos.fetch_by_id(id_carrinho))
            except Carrinhos.DoesNotExist:
                raise NotFound("Carrinho não encontrado")

        # Carrinho atual
        atual = request.GET.get('atual')
        if atual and atual.lower() == 'true': 
            try:
                return Response(Carrinhos.fetch_atual())
            except Carrinhos.DoesNotExist:
                raise NotFound("Carrinho não encontrado")
            
        # Todos os Carrinhos
        return Response(Carrinhos.fetch_all())


# IngredientesCarrinhos
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_ingredientesCarrinhos(request, id_carrinho):
    if request.method == 'GET':
        return Response(IngredientesCarrinhos.fetch_search(id_carrinho, request.GET.get('id_administrador'), request.GET.get('id_ingrediente')))
    elif request.method == 'POST':
        return Response(operacoes.create_ingredientesCarrinhos(id_carrinho, request.data), status=201)

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_ingredientesCarrinhos(request, id_ingrediente_carrinho):
    if request.method == 'PUT':
        return Response(operacoes.update_ingredientesCarrinhos(id_ingrediente_carrinho, request.data))
    elif request.method == 'DELETE':
        operacoes.delete_ingredientesCarrinhos(id_ingrediente_carrinho)
        return Response({"msg": "IngredienteCarrinho apagado"}, status=200)

# UtensiliosCarrinhos
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_utensiliosCarrinhos(request, id_carrinho):
    if request.method == 'GET':
        return Response(UtensiliosCarrinhos.fetch_search(id_carrinho, request.GET.get('id_administrador'), request.GET.get('id_utensilio')))     
    elif request.method == 'POST':
        return Response(operacoes.create_utensiliosCarrinhos(id_carrinho, request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_utensiliosCarrinhos(request, id_utensilio_carrinho):
    if request.method == 'PUT':
        return Response(operacoes.update_utensiliosCarrinhos(id_utensilio_carrinho, request.data), status=200)
    elif request.method == 'DELETE':    
        operacoes.delete_utensiliosCarrinhos(id_utensilio_carrinho)
        return Response({"msg": "UtensilioCarrinho apagado"}, status=200)


# Instruções
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_instrucoes(request, id_receita):
    if request.method == 'GET':
        return Response(Instrucoes.fetch_search(id_receita, request.GET.get('numero_sequencia')))
    elif request.method == 'POST':        
        return Response(operacoes.create_instrucoes(id_receita, request.data), status=201)

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_instrucoes(request, id_instrucao):
    if request.method == 'PUT':
        return Response(operacoes.update_instrucoes(id_instrucao, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_instrucoes(id_instrucao)
        return Response({"msg": "Instrucao apagada"}, status=200)


# Receitas
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_receitas(request):
    if request.method == 'GET':
        # Receita por id
        id_receita = request.GET.get('id_receita')
        if id_receita:
            try:
                return Response(Receitas.fetch_by_id(id_receita))
            except Receitas.DoesNotExist:
                raise Response("Receita não encontrada", status=404)

        # Todas as receitas
        return Response(Receitas.fetch_all())
    
    elif request.method == 'POST':
        return Response(operacoes.create_receitas(request.data), status=201)

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_receitas(request, id_receita):
    if request.method == 'PUT':
        return Response(operacoes.update_receitas(id_receita, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_receitas(id_receita)
        return Response({"msg": "Receita apagada"}, status=200)

# IngredientesReceitas
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_ingredientesReceitas(request, id_receita):
    if request.method == 'GET':
        return Response(IngredientesReceitas.fetch_search(id_receita, request.GET.get('id_ingrediente')))
    elif request.method == 'POST':
        return Response(operacoes.create_ingredientesReceitas(id_receita, request.data), status=201)

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_ingredientesReceitas(request, id_ingrediente_receita):
    if request.method == 'PUT':
        return Response(operacoes.update_ingredientesReceitas(id_ingrediente_receita, request.data), status=200)
    elif request.method == 'DELETE':    
        operacoes.delete_ingredientesReceitas(id_ingrediente_receita)
        return Response({"msg": "IngredienteReceita apagado"}, status=200)

# UtensiliosReceitas
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_post_utensiliosReceitas(request, id_receita):
    if request.method == 'GET':
        return Response(UtensiliosReceitas.fetch_search(id_receita, request.GET.get('id_utensilio')))
    elif request.method == 'POST':
        return Response(operacoes.create_utensiliosReceitas(id_receita, request.data), status=201)

    
@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_utensiliosReceitas(request, id_utensilio_receita):
    if request.method == 'PUT':            
        return Response(operacoes.update_utensiliosReceitas(id_utensilio_receita, request.data), status=200)
    elif request.method == 'DELETE':    
        operacoes.delete_utensiliosReceitas(id_utensilio_receita)
        return Response({"msg": "UtensilioReceita apagado"}, status=200)
    
    