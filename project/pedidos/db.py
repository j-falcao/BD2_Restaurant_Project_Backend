from .models import EstadoMesa, Mesas, Servico, Reservas, Pedidos


def get_all_estados_mesa():
    return EstadoMesa.objects.all()


def get_estado_mesa_by_id(id_estado_mesa):
    return EstadoMesa.objects.get(id_estado_mesa=id_estado_mesa)


def get_all_mesas():
    return Mesas.objects.all()


def get_mesa_by_id(id_mesa):
    return Mesas.objects.get(id_mesa=id_mesa)


def get_all_servicos():
    return Servico.objects.all()


def get_servico_by_id(id_servico):
    return Servico.objects.get(id_servico=id_servico)


def get_all_reservas():
    return Reservas.objects.all()


def get_reserva_by_id(id_reserva):
    return Reservas.objects.get(id_reserva=id_reserva)


def get_all_pedidos():
    return Pedidos.objects.all()


def get_pedido_by_id(id_pedido):
    return Pedidos.objects.get(id_pedido=id_pedido)
