from .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from . import db


@api_view(['GET'])
def get_ingredientes(request):
    ingredientes = db.get_all_ingredientes()
    serializer = IngredienteSerializer(ingredientes, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_ingrediente(request, id_ingrediente):
    ingrediente = db.get_ingrediente_by_id(id_ingrediente)
    serializer = IngredienteSerializer(ingrediente)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_utensilios(request):
    utensilios = db.get_all_utensilios()
    serializer = UtensilioSerializer(utensilios, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_utensilio(request, id_utensilio):
    utensilio = db.get_utensilio_by_id(id_utensilio)
    serializer = UtensilioSerializer(utensilio)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_receitas(request):
    receitas = db.get_all_receitas()
    serializer = ReceitaSerializer(receitas, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_receita(request, id_receita):
    receita = db.get_receita_by_id(id_receita)
    serializer = ReceitaSerializer(receita)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_carrinhos(request):
    carrinhos = db.get_all_carrinhos()
    serializer = CarrinhoSerializer(carrinhos, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_carrinho(request, id_carrinho):
    carrinho = db.get_carrinho_by_id(id_carrinho)
    serializer = CarrinhoSerializer(carrinho)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_fornecedores(request):
    fornecedores = db.get_all_fornecedores()
    serializer = FornecedorSerializer(fornecedores, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_fornecedor(request, id_fornecedor):
    fornecedor = db.get_fornecedor_by_id(id_fornecedor)
    serializer = FornecedorSerializer(fornecedor)
    return JsonResponse(serializer.data, safe=False)