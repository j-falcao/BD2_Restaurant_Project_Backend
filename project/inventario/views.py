from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def ingredientes_view(request):
    return Response([
        {'id': 1, 'name': 'João', 'idade': 22},
        {'id': 2, 'name': 'Maria', 'idade': 24},
        {'id': 3, 'name': 'Jose', 'idade': 23},
    ])