from rest_framework.decorators import api_view
from rest_framework.response import Response
from .operacoes import *

@api_view(['POST'])
def dashboard_view(request):
    return Response(dashboard(request.data))