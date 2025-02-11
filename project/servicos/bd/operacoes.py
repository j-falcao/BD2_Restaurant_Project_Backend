from django.db import connection
from ..models import *
from estatisticas import operacoes as estatisticas


# Mesas
def create_mesas(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_mesas(%s, %s)', [
            data['capacidade_maxima'],
            None
        ])
        return cursor.fetchone()[0]

def update_mesas(id_mesa, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_mesas(%s, %s, %s, %s)', [
            id_mesa,
            data['numero'],
            data['capacidade_maxima'],
            None
        ])
        return cursor.fetchone()[0]

def delete_mesas(id_mesa):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_mesas(%s)', [id_mesa])


# Reservas
def create_reservas(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_reservas(%s, %s, %s, %s, %s, %s)', [
            data['id_mesa'],
            data['quantidade_pessoas'],
            data['observacoes'],
            data['id_garcom'],
            data['data_hora'],
            None
        ])

        estatisticas.create_reserva(data)
        return cursor.fetchone()[0]

def update_reservas(id_reserva, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_reservas(%s, %s, %s, %s, %s, %s, %s, %s)', [
            id_reserva,
            data['id_mesa'],
            data['id_estado_reserva'],
            data['quantidade_pessoas'],
            data['observacoes'],
            data['id_garcom'],
            data['data_hora'],
            None
        ])
        return cursor.fetchone()[0]

def cancelar_reservas(id_reserva):
    with connection.cursor() as cursor:
        cursor.execute('CALL cancelar_reservas(%s, %s)', [
            id_reserva,
            None
        ])
        return cursor.fetchone()[0]

def delete_reservas(id_reserva):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_reservas(%s)', [id_reserva])


# Servicos
def create_servicos(data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_servicos(%s, %s, %s)', [
            data['id_garcom'],
            data['id_mesa'],
            None
        ])

        estatisticas.create_servico(data)
        return cursor.fetchone()[0]

def update_servicos(id_servico, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_servicos(%s, %s, %s, %s)', [
            id_servico,
            data['id_garcom'],
            data['id_mesa'],
            None
        ])
        return cursor.fetchone()[0]

def concluir_servicos(id_servico):
    with connection.cursor() as cursor:
        cursor.execute('CALL concluir_servicos(%s, %s)', [
            id_servico, None
        ])
        return cursor.fetchone()[0]

def create_servico_com_reserva(id_reserva):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_servico_com_reserva(%s, %s)', [
            id_reserva,
            None
        ])
        return cursor.fetchone()[0]

def delete_servicos(id_servico):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_servicos(%s)', [id_servico])


# Pedidos
def create_pedidos(id_servico):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_pedidos(%s, %s)', [
            id_servico,
            None
        ])
        return cursor.fetchone()[0]

def delete_pedidos(id_pedido):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_pedidos(%s)', [id_pedido])


# PedidosProdutos
def create_pedidosProdutos(id_pedido, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL create_pedidosprodutos(%s, %s, %s, %s)', [
            id_pedido,
            data['quantidade'],
            data['id_produto'],
            None
        ])
        return cursor.fetchone()[0]

def escolher_pedidosProdutos(id_pedido_produto, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL escolher_pedidosprodutos(%s, %s, %s)', [
            id_pedido_produto,
            data['id_cozinheiro'],
            None
        ])
        return cursor.fetchone()[0]

def confecionar_pedidosProdutos(id_pedido_produto):
    with connection.cursor() as cursor:
        cursor.execute('CALL confecionar_pedidosprodutos(%s, %s)', [
            id_pedido_produto,
            None
        ])

        return cursor.fetchone()[0]
    
def update_pedidosProdutos(id_pedido_produto, data):
    with connection.cursor() as cursor:
        cursor.execute('CALL update_pedidosprodutos(%s, %s, %s)', [
            id_pedido_produto,
            data['quantidade'],
            None
        ])
        return cursor.fetchone()[0]

def delete_pedidosProdutos(id_pedido_produto):
    with connection.cursor() as cursor:
        cursor.execute('CALL delete_pedidosprodutos(%s)', [id_pedido_produto])
