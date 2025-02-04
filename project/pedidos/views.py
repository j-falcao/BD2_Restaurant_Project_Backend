from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *
from . import db

@api_view(['GET', 'POST'])
def get_post_estados_mesas(request):
    if request.method == 'GET':
        return Response(EstadosMesas.fetch_all())
    elif request.method == 'POST':
        return Response(db.create_estadosMesas(request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
def update_delete_estados_mesas(request, id_estado_mesa):
    if request.method == 'PUT':
        return Response(db.update_estadosMesas(id_estado_mesa, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_estadosMesas(id_estado_mesa)
        return Response({"msg": "EstadoMesa apagado"}, status=200)
    

@api_view(['GET', 'POST'])
def get_post_mesas(request):
    if request.method == 'GET':
        id_mesa = request.GET.get('id_mesa')
        if id_mesa:
            try:
                return Response(Mesas.fetch_by_id(id_mesa))
            except Mesas.DoesNotExist:
                raise NotFound("Mesa nao encontrada")
        else:
            return Response(Mesas.fetch_all())
    elif request.method == 'POST':
        return Response(db.create_mesas(request.data), status=201)
    
@api_view(['PUT', 'DELETE'])
def update_delete_mesas(request, id_mesa):
    if request.method == 'PUT':
        return Response(db.update_mesas(id_mesa, request.data), status=200)
    elif request.method == 'DELETE':
        db.delete_mesas(id_mesa)
        return Response({"msg": "Mesa apagada"}, status=200)
    

@api_view(['GET', 'POST'])
def get_post_servicos(request):
    if request.method == 'GET':
        return Response(Servicos.fetch_all())
    elif request.method == 'POST':
        return Response(db.create_servicos(request.data), status=201)
    
@api_view(['POST'])
def concluir_servicos(request, id_servico):
    return Response(db.concluir_servicos(id_servico), status=200)
    
@api_view(['POST'])
def post_servico_com_reserva(request, id_reserva):
    return Response(db.create_servico_com_reserva(id_reserva), status=201)

@api_view(['PUT', 'DELETE'])
def update_delete_servicos(request, id_servico):
    if request.method == 'PUT':        
        return Response(db.update_servicos(id_servico, request.data), status=200)
    elif request.method == 'DELETE':        
        db.delete_servicos(id_servico)
        return Response({"msg": "Servico apagado"}, status=200)
    

@api_view(['GET', 'POST'])
def get_post_pedidos(request, id_servico):
    if request.method == 'GET':
        return Response(Pedidos.fetch_by_servico(id_servico), status=200)
    elif request.method == 'POST':
        return Response(db.create_pedidos(id_servico), status=201)
    
@api_view(['DELETE'])
def delete_pedidos(request, id_pedido):
    db.delete_pedidos(id_pedido)
    return Response({"msg": "Pedido apagado"}, status=200)

@api_view(['GET', 'POST'])
def get_post_pedidosProdutos(request, id_pedido):
    if request.method == 'GET':
        return Response(PedidosProdutos.fetch_by_pedido(id_pedido))
    elif request.method == 'POST':
        return Response(db.create_pedidosProdutos(id_pedido, request.data), status=201)

@api_view(['POST'])
def confecionar_pedidosProdutos(request, id_pedido_produto):
    return Response(db.confeccionar_pedidosProdutos(id_pedido_produto, request.data), status=200)
    
@api_view(['DELETE'])
def delete_pedidosProdutos(request, id_pedido_produto):
    db.delete_pedidosProdutos(id_pedido_produto)
    return Response({"msg": "PedidoProduto apagado"}, status=200)


@api_view(['GET', 'POST'])
def get_post_reservas(request):
    if request.method == 'GET':
        id_reserva = request.GET.get('id_reserva')
        if id_reserva:
            try:
                return Response(Reservas.fetch_by_id(id_reserva))
            except Reservas.DoesNotExist:
                raise NotFound("Reserva nao encontrada")
        else:
            return Response(Reservas.fetch_all())
    elif request.method == 'POST':
        return Response(db.create_reservas(request.data), status=201)
    
@api_view(['POST'])
def cancelar_reservas(request, id_reserva):
    return Response(db.cancelar_reservas(id_reserva), status=200)
    
@api_view(['PUT', 'DELETE'])    
def update_delete_reservas(request, id_reserva):
    if request.method == 'PUT':        
        return Response(db.update_reservas(id_reserva, request.data), status=200)
    elif request.method == 'DELETE':        
        db.delete_reservas(id_reserva)
        return Response({"msg": "Reserva apagada"}, status=200)