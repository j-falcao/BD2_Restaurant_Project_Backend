from rest_framework.decorators import api_view
from rest_framework.response import Response
from .bd import *

@api_view(['GET'])
def dashboard_view(request):
    return Response(dashboard())