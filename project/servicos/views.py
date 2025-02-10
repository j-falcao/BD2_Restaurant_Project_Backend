from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *
from .bd import operacoes


# Mesas
@api_view(['GET'])
def get_estadosmesas(request):
    return Response(EstadosMesas.fetch_all())

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

@api_view(['GET'])
def get_servicos_ativos(request):
    return Response(Servicos.fetch_ativos())

@api_view(['GET'])
def get_servico_com_pedidos(request, id_servico):
    return Response(Servicos.fetch_com_pedidos(id_servico))

@api_view(['POST'])
def concluir_servicos(request, id_servico):
    return Response(operacoes.concluir_servicos(id_servico), status=200)

@api_view(['POST'])
def post_servico_com_reserva(request, id_reserva):
    return Response(operacoes.create_servico_com_reserva(id_reserva), status=201)

@api_view(['GET'])
def get_servicos_by_garcom(request, id_garcom):
    return Response(Servicos.fetch_by_garcom(id_garcom))

@api_view(['GET'])
def get_servicos_by_mesa(request, id_mesa):
    return Response(Servicos.fetch_by_mesa(id_mesa))

@api_view(['GET'])
def get_servicos_by_data(request):
    data_hora_inicio = request.GET.get('data_hora_inicio')
    data_hora_fim = request.GET.get('data_hora_fim')
    if data_hora_inicio is None or data_hora_fim is None:
        raise NotFound({"msg": "Data e hora inicio e fim sao obrigatorios"})
    return Response(Servicos.fetch_by_data(data_hora_inicio, data_hora_fim))

@api_view(['PUT', 'DELETE'])
def update_delete_servicos(request, id_servico):
    if request.method == 'PUT':
        return Response(operacoes.update_servicos(id_servico, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_servicos(id_servico)
        return Response({"msg": "Servico apagado"}, status=200)


# Pedidos
@api_view(['POST'])
def post_pedidos(request, id_servico):
    return Response(operacoes.create_pedidos(id_servico), status=201)

@api_view(['DELETE'])
def delete_pedidos(request, id_pedido):
    operacoes.delete_pedidos(id_pedido)
    return Response({"msg": "Pedido apagado"}, status=200)


# PedidosProdutos
@api_view(['GET'])
def get_estadospedidosprodutos(request):
    return Response(EstadosPedidosProdutos.fetch_all())

@api_view(['POST'])
def post_pedidosprodutos(request, id_pedido):
    return Response(operacoes.create_pedidosProdutos(id_pedido, request.data), status=201)

@api_view(['POST'])
def confecionar_pedidosprodutos(request, id_pedido_produto):
    return Response(operacoes.confecionar_pedidosProdutos(id_pedido_produto), status=200)

@api_view(['POST'])
def escolher_pedidosprodutos(request, id_pedido_produto):
    return Response(operacoes.escolher_pedidosProdutos(id_pedido_produto, request.data), status=200)

@api_view(['PUT', 'DELETE'])
def update_delete_pedidosprodutos(request, id_pedido_produto):
    if request.method == 'PUT':
        return Response(operacoes.update_pedidosProdutos(id_pedido_produto, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_pedidosProdutos(id_pedido_produto)
        return Response({"msg": "PedidoProduto apagado"}, status=200)


# Reservas
@api_view(['GET'])
def get_estadosreservas(request):
    return Response(EstadosReservas.fetch_all())

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


@api_view(['GET'])
def get_reservas_by_mesa(request, id_mesa):
    return Response(Reservas.fetch_by_mesa(id_mesa))


@api_view(['GET'])
def get_reservas_by_garcom(request, id_garcom):
    return Response(Reservas.fetch_by_garcom(id_garcom))


@api_view(['GET'])
def get_reservas_by_data(request):
    data_hora_inicio = request.GET.get('data_hora_inicio')
    data_hora_fim = request.GET.get('data_hora_fim')
    if data_hora_inicio is None or data_hora_fim is None:
        raise NotFound({"msg": "Data e hora inicio e fim sao obrigatorios"})
    return Response(Reservas.fetch_by_data(data_hora_inicio, data_hora_fim))


@api_view(['PUT', 'DELETE'])
def update_delete_reservas(request, id_reserva):
    if request.method == 'PUT':
        return Response(operacoes.update_reservas(id_reserva, request.data), status=200)
    elif request.method == 'DELETE':
        operacoes.delete_reservas(id_reserva)
        return Response({"msg": "Reserva apagada"}, status=200)
