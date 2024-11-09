from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import db


@api_view(['GET'])
def get_ingredientes(request):
    return Response(db.get_all_ingredientes())

@api_view(['GET'])
def get_ingrediente(request, id_ingrediente):
    return Response(db.get_ingrediente_by_id(id_ingrediente))


@api_view(['GET'])
def get_utensilios(request):
    return Response(db.get_all_utensilios())

@api_view(['GET'])
def get_utensilio(request, id_utensilio):
    return Response(db.get_utensilio_by_id(id_utensilio))


@api_view(['GET'])
def get_receitas(request):
    return Response(db.get_all_receitas())

@api_view(['GET'])
def get_receita(request, id_receita):
    return Response(db.get_receita_by_id(id_receita))


@api_view(['GET'])
def get_carrinhos(request):
    return Response(db.get_all_carrinhos())

@api_view(['GET'])
def get_carrinho(request, id_carrinho):
    return Response(db.get_carrinho_by_id(id_carrinho))


@api_view(['GET'])
def get_fornecedores(request):
    return Response(db.get_all_fornecedores())

@api_view(['GET'])
def get_fornecedor(request, id_fornecedor):
    return Response(db.get_fornecedor_by_id(id_fornecedor))