from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def ingredientes_view(request):
    return Response([{'name': 'João', 'idade': 22}])