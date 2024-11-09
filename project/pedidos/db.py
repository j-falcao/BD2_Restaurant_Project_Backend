from .models import EstadoMesa, Mesa, Servico, Reserva, Pedido

def get_all_estados_mesa():
    return EstadoMesa.objects.all()

def get_estado_mesa_by_id(id_estado_mesa):
    return EstadoMesa.objects.get(id=id_estado_mesa)


def get_all_mesas():
    return Mesa.objects.all()

def get_mesa_by_id(id_mesa):
    return Mesa.objects.get(id=id_mesa)


def get_all_servicos():
    return Servico.objects.all()

def get_servico_by_id(id_servico):
    return Servico.objects.get(id=id_servico)


def get_all_reservas():
    return Reserva.objects.all()

def get_reserva_by_id(id_reserva):
    return Reserva.objects.get(id=id_reserva)


def get_all_pedidos():
    return Pedido.objects.all()

def get_pedido_by_id(id_pedido):
    return Pedido.objects.get(id=id_pedido)
