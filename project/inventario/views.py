from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import db
# ✅


@api_view(['GET', 'POST'])
def get_post_ingredientes(request):
    if request.method == 'GET':
        id_ingrediente = request.GET.get('id_ingrediente')

        if id_ingrediente:
            try:
                ingrediente = db.get_ingredientes(id_ingrediente)
                serializer = IngredientesSerializer(ingrediente)
                return Response(serializer.data)
            except Ingredientes.DoesNotExist:
                raise Response("Ingrediente não encontrado", status=404)
        else:
            ingredientes = db.get_ingredientes()
            serializer = IngredientesSerializer(ingredientes, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientesSerializer(data=request.data)
        if serializer.is_valid():
            db.create_ingredientes(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_ingredientes(request, id_ingrediente):
    ingrediente = db.get_ingredientes(id_ingrediente)
    if (not ingrediente):
        raise Response("Ingrediente nao encontrado", status=404)

    if request.method == 'PUT':
        serializer = IngredientesSerializer(ingrediente)
        if serializer.is_valid():
            db.update_ingredientes(serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            db.delete_ingredientes(ingrediente)
            return Response({"msg": "Ingrediente apagado"}, status=200)
        except Ingredientes.DoesNotExist:
            raise Response("Ingrediente não encontrado", status=404)


@api_view(['GET', 'POST'])
def get_post_utensilios(request):
    if request.method == 'GET':
        id_utensilio = request.GET.get('id_utensilio')

        if id_utensilio:
            try:
                utensilio = db.get_utensilio_by_id(id_utensilio)
                serializer = UtensiliosSerializer(utensilio)
                return Response(serializer.data)
            except Utensilios.DoesNotExist:
                raise Response("Utensílio não encontrado", status=404)
        else:
            utensilios = db.get_all_utensilios()
            serializer = UtensiliosSerializer(utensilios, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UtensiliosSerializer(data=request.data)
        if serializer.is_valid():
            db.create_utensilio(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update_delete_utensilios(request, id_ingrediente):
    utensilio = db.get_utensilios(id_ingrediente)
    if not utensilio:
        raise Response("Utensílio não encontrado", status=404)

    if request.method == 'PUT':
        try:
            serializer = IngredientesSerializer(utensilio)
            if serializer.is_valid():
                db.update_utensilios(serializer.validated_data)
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Ingredientes.DoesNotExist:
            raise Response("Ingrediente não encontrado", status=404)

    elif request.method == 'DELETE':
        try:
            db.delete_ingredientes(ingrediente)
            return Response({"msg": "Ingrediente apagado"}, status=200)
        except Ingredientes.DoesNotExist:
            raise Response("Ingrediente não encontrado", status=404)


@api_view(['GET'])
def get_receitas(request):
    receitas = db.get_all_receitas()
    serializer = ReceitasSerializer(receitas, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_receita(request, id_receita):
    print('OOOOOOOOOOOOOOOOOOO')
    receita = db.get_receita_by_id(id_receita)
    serializer = ReceitasSerializer(receita)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_carrinhos(request):
    carrinhos = db.get_all_carrinhos()
    serializer = CarrinhosSerializer(carrinhos, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_carrinho(request, id_carrinho):
    carrinho = db.get_carrinho_by_id(id_carrinho)
    serializer = CarrinhosSerializer(carrinho)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_fornecedores(request):
    fornecedores = db.get_all_fornecedores()
    serializer = FornecedoresSerializer(fornecedores, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_fornecedor(request, id_fornecedor):
    fornecedor = db.get_fornecedor_by_id(id_fornecedor)
    serializer = FornecedoresSerializer(fornecedor)
    return JsonResponse(serializer.data, safe=False)
