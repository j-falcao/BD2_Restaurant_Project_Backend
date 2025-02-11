from rest_framework.decorators import api_view
from rest_framework.response import Response
from .operacoes_recolha import *

@api_view(['GET'])
def percentagem_tipos(request):
    return Response(percentagem_ingredientes_por_tipo(), status=200)