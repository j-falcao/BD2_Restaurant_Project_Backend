from rest_framework.decorators import api_view
from rest_framework.response import Response
from .operacoes import *

@api_view(['GET'])
def get_tipos_itens_mais_usados(request):
    return Response(operacoes.tipos_itens_mais_usados())