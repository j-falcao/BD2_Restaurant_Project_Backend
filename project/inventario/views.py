from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from . import db

# Ingredientes
@api_view(['GET', 'POST'])
def get_post_ingredientes(request): #✅
    if request.method == 'GET':
        id_ingrediente = request.GET.get('id_ingrediente')

        if id_ingrediente:
            try:
                ingrediente = db.get_ingredientes(id_ingrediente)
                serializer = IngredientesSerializer(ingrediente)
                return Response(serializer.data)
            except Ingredientes.DoesNotExist:
                raise NotFound("Ingrediente não encontrado")
        else:
            ingredientes = db.get_ingredientes()
            serializer = IngredientesSerializer(ingredientes, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_ingredientes(request, id_ingrediente): #✅
    try:
        ingrediente_old = db.get_ingredientes(id_ingrediente)
    except Ingredientes.DoesNotExist:
        raise NotFound("Ingrediente nao encontrado")

    if request.method == 'PUT':
        serializer = IngredientesSerializer(ingrediente_old, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        db.delete_ingredientes(id_ingrediente)
        return Response({"msg": "Ingrediente apagado"}, status=204)


# Utensílios ✅
@api_view(['GET', 'POST'])
def get_post_utensilios(request): #✅
    if request.method == 'GET':
        id_utensilio = request.GET.get('id_utensilio')

        if id_utensilio:
            try:
                utensilio = db.get_utensilios(id_utensilio)
                serializer = UtensiliosSerializer(utensilio)
                return Response(serializer.data)
            except Utensilios.DoesNotExist:
                raise NotFound("Utensílio não encontrado")
        else:
            utensilios = db.get_utensilios()
            serializer = UtensiliosSerializer(utensilios, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UtensiliosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_utensilios(request, id_utensilio): #✅
    try:
        utensilio_old = db.get_utensilios(id_utensilio)
    except:
        raise NotFound("Utensílio não encontrado")

    if request.method == 'PUT':
        serializer = UtensiliosSerializer(utensilio_old, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        db.delete_utensilios(id_utensilio)
        return Response({"msg": "Utensílio apagado"}, status=200)


# Fornecedores
@api_view(['GET', 'POST'])
def get_post_fornecedores(request): #✅
    if request.method == 'GET':
        id_fornecedor = request.GET.get('id_fornecedor')

        if id_fornecedor:
            try:
                fornecedor = db.get_fornecedores(id_fornecedor)
                serializer = FornecedoresSerializer(fornecedor)
                return Response(serializer.data)
            except Fornecedores.DoesNotExist:
                raise NotFound("Fornecedor nao encontrado")
        else:
            fornecedores = db.get_fornecedores()
            serializer = FornecedoresSerializer(fornecedores, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FornecedoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_fornecedores(request, id_fornecedor): #✅
    try:
        fornecedor_old = db.get_fornecedores(id_fornecedor)
    except:
        raise NotFound("Fornecedor nao encontrado")

    if request.method == 'PUT':
        serializer = FornecedoresSerializer(fornecedor_old, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        db.delete_fornecedores(id_fornecedor)
        return Response({"msg": "Fornecedor apagado"}, status=200)


# Carrinhos
@api_view(['GET'])
def get_carrinhos(request):
    if request.method == 'GET':

        # Carrinho atual
        atual = request.GET.get('atual')
        if atual != None and atual == 'true': 
            try:
                carrinho = db.get_carrinhos(atual=True)
                serializer = CarrinhosSerializer(carrinho)
                return Response(serializer.data)
            except Carrinhos.DoesNotExist:
                raise NotFound("Carrinho não encontrado")

        # Carrinho por id
        id_carrinho = request.GET.get('id_carrinho')
        if id_carrinho:
            try:
                carrinho = db.get_carrinhos(id_carrinho)
                serializer = CarrinhosSerializer(carrinho)
                return Response(serializer.data)
            except Carrinhos.DoesNotExist:
                raise Response("Carrinho não encontrado", status=404)
        
        # Carrinhos todos
        carrinhos = db.get_carrinhos()
        serializer = CarrinhosSerializer(carrinhos, many=True)
        return Response(serializer.data)


# IngredientesCarrinhos
@api_view(['GET', 'POST'])
def get_post_ingredientesCarrinhos(request):
    if request.method == 'GET':
        id_ingrediente_carrinho = request.GET.get('id_ingrediente_carrinho')

        if id_ingrediente_carrinho:
            try:
                ingredienteCarrinho = db.get_ingredientesCarrinhos(id_ingrediente_carrinho)
                serializer = IngredientesCarrinhosSerializer(ingredienteCarrinho)
                return Response(serializer.data)
            except IngredientesCarrinhos.DoesNotExist:
                raise Response("IngredientesCarrinhos nao encontrado", status=404)
        else:
            ingredienteCarrinho = db.get_ingredientesCarrinhos()
            serializer = IngredientesCarrinhosSerializer(ingredienteCarrinho, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientesCarrinhosSerializer(data=request.data)
        if serializer.is_valid():
            db.create_ingredientesCarrinhos(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_ingredientesCarrinhos(request, id_ingrediente_carrinho):
    ingredienteCarrinho = db.get_ingredientesCarrinhos(id_ingrediente_carrinho)
    if not ingredienteCarrinho:
        raise Response("IngredienteCarrinho não encontrado", status=404)

    if request.method == 'PUT':
        serializer = IngredientesCarrinhosSerializer(ingredienteCarrinho)
        if serializer.is_valid():
            db.update_ingredientesCarrinhos(ingredienteCarrinho, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        db.delete_ingredientesCarrinhos(id_ingrediente_carrinho)
        return Response({"msg": "IngredienteCarrinho apagado"}, status=200)
    

# UtensiliosCarrinhos
@api_view(['GET', 'POST'])
def get_post_utensiliosCarrinhos(request):
    if request.method == 'GET':
        id_utensilio_carrinho = request.GET.get('id_utensilio_carrinho')

        if id_utensilio_carrinho:
            try:
                utensilioCarrinho = db.get_utensiliosCarrinhos(id_utensilio_carrinho)
                serializer = UtensiliosCarrinhosSerializer(utensilioCarrinho)
                return Response(serializer.data)
            except UtensiliosCarrinhos.DoesNotExist:
                raise Response("UtensilioCarrinho não encontrado", status=404)
        else:
            utensilioCarrinho = db.get_utensiliosCarrinhos()
            serializer = UtensiliosCarrinhosSerializer(utensilioCarrinho, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UtensiliosCarrinhosSerializer(data=request.data)
        if serializer.is_valid():
            db.create_utensiliosCarrinhos(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['PUT', 'DELETE'])
def update_delete_utensiliosCarrinhos(request, id_utensilio_carrinho):
    utensilioCarrinho = db.get_utensiliosCarrinhos(id_utensilio_carrinho)
    if not utensilioCarrinho:
        raise Response("UtensilioCarrinho não encontrado", status=404)

    if request.method == 'PUT':
        serializer = UtensiliosCarrinhosSerializer(utensilioCarrinho)
        if serializer.is_valid():
            db.update_utensiliosCarrinhos(id_utensilio_carrinho, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':    
        db.delete_utensiliosCarrinhos(id_utensilio_carrinho)
        return Response({"msg": "UtensilioCarrinho apagado"}, status=200)


# Receitas
@api_view(['GET', 'POST'])
def get_post_receitas(request):
    if request.method == 'GET':
        id_receita = request.GET.get('id_receita')

        if id_receita:
            try:
                receita = db.get_receitas(id_receita)
                serializer = ReceitasSerializer(receita)
                return Response(serializer.data)
            except Receitas.DoesNotExist:
                raise Response("Receita não encontrada", status=404)
        else:
            receitas = db.get_receitas()
            serializer = ReceitasSerializer(receitas, many=True)
            print(serializer.data)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReceitasSerializer(data=request.data)
        if serializer.is_valid():
            db.create_receitas(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_receitas(request, id_receita):
    receita = db.get_receitas(id_receita)
    if not receita:
        raise Response("Receita nao encontrada", status=404)

    if request.method == 'PUT':
        serializer = ReceitasSerializer(receita)
        if serializer.is_valid():
            db.update_receitas(id_receita, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        db.delete_receitas(id_receita)
        return Response({"msg": "Receita apagada"}, status=200)


# UtensiliosReceitas
@api_view(['GET', 'POST'])
def get_post_utensiliosReceitas(request):
    if request.method == 'GET':
        id_utensilio_receita = request.GET.get('id_utensilio_receita')

        if id_utensilio_receita:
            try:
                utensilioReceita = db.get_utensiliosReceitas(id_utensilio_receita)
                serializer = UtensiliosReceitasSerializer(utensilioReceita)
                return Response(serializer.data)
            except UtensiliosReceitas.DoesNotExist:
                raise Response("UtensilioReceita não encontrado", status=404)
        else:
            utensilioReceita = db.get_utensiliosReceitas()
            serializer = UtensiliosReceitasSerializer(utensilioReceita, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UtensiliosReceitasSerializer(data=request.data)
        if serializer.is_valid():
            db.create_utensiliosReceitas(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['PUT', 'DELETE'])
def update_delete_utensiliosReceitas(request, id_utensilio_receita):
    utensilioReceita = db.get_utensiliosReceitas(id_utensilio_receita)
    if not utensilioReceita:
        raise Response("UtensilioReceita nao encontrado", status=404)

    if request.method == 'PUT':
        serializer = UtensiliosReceitasSerializer(utensilioReceita)
        if serializer.is_valid():
            db.update_utensiliosReceitas(id_utensilio_receita, serializer.validated_data)            
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':    
        db.delete_utensiliosReceitas(id_utensilio_receita)
        return Response({"msg": "UtensilioReceita apagado"}, status=200)
    

# IngredientesReceitas
@api_view(['GET', 'POST'])
def get_post_ingredientesReceitas(request):
    if request.method == 'GET':
        id_ingrediente_receita = request.GET.get('id_ingrediente_receita')

        if id_ingrediente_receita:
            try:
                ingredienteReceita = db.get_ingredientesReceitas(id_ingrediente_receita)
                serializer = IngredientesReceitasSerializer(ingredienteReceita)
                return Response(serializer.data)
            except IngredientesReceitas.DoesNotExist:
                raise Response("IngredienteReceita não encontrado", status=404)
        else:
            ingredienteReceita = db.get_ingredientesReceitas()
            serializer = IngredientesReceitasSerializer(ingredienteReceita, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientesReceitasSerializer(data=request.data)
        if serializer.is_valid():
            db.create_ingredientesReceitas(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['PUT', 'DELETE'])
def update_delete_ingredientesReceitas(request, id_ingrediente_receita):
    ingredienteReceita = db.get_ingredientesReceitas(id_ingrediente_receita)
    if not ingredienteReceita:
        raise Response("IngredienteReceita nao encontrado", status=404)

    if request.method == 'PUT':
        serializer = IngredientesReceitasSerializer(ingredienteReceita)
        if serializer.is_valid():
            db.update_ingredientesReceitas(id_ingrediente_receita, serializer.validated_data)            
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':    
        db.delete_ingredientesReceitas(id_ingrediente_receita)
        return Response({"msg": "IngredienteReceita apagado"}, status=200)


# Instruções
@api_view(['GET', 'POST'])
def get_post_instrucoes(request):
    if request.method == 'GET':
        id_instrucao = request.GET.get('id_instrucao')

        if id_instrucao:
            try:
                instrucao = db.get_instrucoes(id_instrucao)
                serializer = InstrucoesSerializer(instrucao)
                return Response(serializer.data)
            except Instrucoes.DoesNotExist:
                raise Response("Instrução não encontrada", status=404)
        else:
            instrucoes = db.get_instrucoes()
            serializer = InstrucoesSerializer(instrucoes, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':        
        serializer = InstrucoesSerializer(data=request.data)
        if serializer.is_valid():
            db.create_instrucoes(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_instrucoes(request, id_instrucao):
    instrucao = db.get_instrucoes(id_instrucao)
    if not instrucao:
        raise Response("Instrução não encontrada", status=404)    

    if request.method == 'PUT':
        serializer = InstrucoesSerializer(instrucao)
        if serializer.is_valid():
            db.update_instrucoes(id_instrucao, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        db.delete_instrucoes(id_instrucao)
        return Response({"msg": "Instrução apagada"}, status=200)