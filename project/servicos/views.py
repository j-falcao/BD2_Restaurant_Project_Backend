from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *
from .bd import operacoes


# Estados Mesas
@api_view(['GET', 'POST'])
def get_post_estadosmesas(request):
    if request.method == 'GET':
        return Response(EstadosMesas.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_estadosMesas(request.data), status=201)


@api_view(['PUT', 'DELETE'])
def update_delete_estadosmesas(request, id_estado_mesa):
    if request.method == 'PUT':
        return Response(operacoes.update_estadosMesas(id_estado_mesa, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_estadosMesas(id_estado_mesa)
        return Response({"msg": "EstadoMesa apagado"}, status=200)


# Mesas
@api_view(['GET', 'POST'])
def get_post_mesas(request):
    if request.method == 'GET':
        return Response(Mesas.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_mesas(request.data), status=201)

@api_view(['GET'])
def get_mesas_disponiveis(request):
    return Response(Mesas.fetch_disponiveis())

@api_view(['GET'])
def get_mesas_ocupadas(request):
    return Response(Mesas.fetch_ocupadas())

@api_view(['GET'])
def get_mesas_reservadas(request):
    return Response(Mesas.fetch_reservadas())

@api_view(['PUT', 'DELETE'])
def update_delete_mesas(request, id_mesa):
    if request.method == 'PUT':
        return Response(operacoes.update_mesas(id_mesa, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_mesas(id_mesa)
        return Response({"msg": "Mesa apagada"}, status=200)


# Servicos
@api_view(['GET', 'POST'])
def get_post_servicos(request):
    if request.method == 'GET':
        return Response(Servicos.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_servicos(request.data), status=201)


@api_view(['POST'])
def concluir_servicos(request, id_servico):
    operacoes.concluir_servicos(id_servico)
    return Response({"msg": "Servico concluido"}, status=200)

@api_view(['POST'])
def post_servico_com_reserva(request, id_reserva):
    return Response(operacoes.create_servico_com_reserva(id_reserva), status=201)


@api_view(['PUT', 'DELETE'])
def update_delete_servicos(request, id_servico):
    if request.method == 'PUT':
        return Response(operacoes.update_servicos(id_servico, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_servicos(id_servico)
        return Response({"msg": "Servico apagado"}, status=200)


# Pedidos
@api_view(['GET', 'POST'])
def get_post_pedidos(request, id_servico):
    if request.method == 'GET':
        return Response(Pedidos.fetch_by_servico(id_servico), status=200)
    elif request.method == 'POST':
        return Response(operacoes.create_pedidos(id_servico), status=201)


@api_view(['DELETE'])
def delete_pedidos(request, id_pedido):
    operacoes.delete_pedidos(id_pedido)
    return Response({"msg": "Pedido apagado"}, status=200)


# PedidosProdutos
@api_view(['GET', 'POST'])
def get_post_pedidosProdutos(request, id_pedido):
    if request.method == 'GET':
        return Response(PedidosProdutos.fetch_by_pedido(id_pedido))
    elif request.method == 'POST':
        return Response(operacoes.create_pedidosProdutos(id_pedido, request.data), status=201)


@api_view(['POST'])
def confecionar_pedidosProdutos(request, id_pedido_produto):
    operacoes.confecionar_pedidosProdutos(id_pedido_produto, request.data)
    return Response({"msg": "PedidoProduto confecionado"}, status=200)


@api_view(['DELETE'])
def delete_pedidosProdutos(request, id_pedido_produto):
    operacoes.delete_pedidosProdutos(id_pedido_produto)
    return Response({"msg": "PedidoProduto apagado"}, status=200)


# Estados Reservas
@api_view(['GET', 'POST'])
def get_post_estadosreservas(request):
    if request.method == 'GET':
        return Response(EstadosReservas.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_estadosReservas(request.data), status=201)


@api_view(['PUT', 'DELETE'])
def update_delete_estadosreservas(request, id_estado_reserva):
    if request.method == 'PUT':
        return Response(operacoes.update_estadosReservas(id_estado_reserva, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_estadosReservas(id_estado_reserva)
        return Response({"msg": "EstadoReserva apagado"}, status=200)


# Reservas
@api_view(['GET', 'POST'])
def get_post_reservas(request):
    if request.method == 'GET':
        return Response(Reservas.fetch_all())
    elif request.method == 'POST':
        return Response(operacoes.create_reservas(request.data), status=201)

@api_view(['GET'])
def get_reservas_confirmadas(request):
    return Response(Reservas.fetch_confirmadas())

@api_view(['GET'])
def get_reservas_canceladas(request):
    return Response(Reservas.fetch_canceladas())

@api_view(['GET'])
def get_reservas_concluidas(request):
    return Response(Reservas.fetch_concluidas())

@api_view(['POST'])
def cancelar_reservas(request, id_reserva):
    operacoes.cancelar_reservas(id_reserva)
    return Response({"msg": "Reserva cancelada"}, status=200)

@api_view(['PUT', 'DELETE'])
def update_delete_reservas(request, id_reserva):
    if request.method == 'PUT':
        return Response(operacoes.update_reservas(id_reserva, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_reservas(id_reserva)
        return Response({"msg": "Reserva apagada"}, status=200)
