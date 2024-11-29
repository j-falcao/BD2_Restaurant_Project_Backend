from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import *
from . import db

@api_view(['GET'])
def get_estados_mesa(request):
    estados_mesa = db.get_all_estados_mesa()
    serializer = EstadoMesaSerializer(estados_mesa, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_estado_mesa(request, id_estado_mesa):
    estado_mesa = db.get_estado_mesa_by_id(id_estado_mesa)
    serializer = EstadoMesaSerializer(estado_mesa)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_mesas(request):
    mesas = db.get_all_mesas()
    serializer = MesasSerializer(mesas, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_mesa(request, id_mesa):
    mesa = db.get_mesa_by_id(id_mesa)
    serializer = MesasSerializer(mesa)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_servicos(request):
    servicos = db.get_all_servicos()
    serializer = ServicosSerializer(servicos, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_servico(request, id_servico):
    servico = db.get_servico_by_id(id_servico)
    serializer = ServicosSerializer(servico)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_reservas(request):
    reservas = db.get_all_reservas()
    serializer = ReservasSerializer(reservas, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_reserva(request, id_reserva):
    reserva = db.get_reserva_by_id(id_reserva)
    serializer = ReservasSerializer(reserva)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_pedidos(request):
    pedidos = db.get_all_pedidos()
    serializer = PedidosSerializer(pedidos, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_pedido(request, id_pedido):
    pedido = db.get_pedido_by_id(id_pedido)
    serializer = PedidosSerializer(pedido)
    return JsonResponse(serializer.data, safe=False)
