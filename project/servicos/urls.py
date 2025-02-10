from django.urls import path
from .views import *

urlpatterns = [
    # estados mesas
    path('estadosmesas/', get_estadosmesas),

    # mesas
    path('mesas/', get_post_mesas),
    path('mesas/<int:id_mesa>/', update_delete_mesas),
    path('mesas/disponiveis/', get_mesas_disponiveis),
    path('mesas/ocupadas/', get_mesas_ocupadas),
    path('mesas/reservadas/', get_mesas_reservadas),
    path('mesas/<int:id_mesa>/servicos/', get_servicos_by_mesa),
    path('mesas/<int:id_mesa>/mesas/', get_reservas_by_mesa),

    # servicos
    path('', get_post_servicos),
    path('data/', get_servicos_by_data),
    path('ativos/', get_servicos_ativos),
    path('<int:id_servico>/pedidosprodutos/', get_servico_com_pedidos),
    path('<int:id_servico>/', update_delete_servicos),
    path('<int:id_servico>/concluir/', concluir_servicos),
    path('<int:id_servico>/pedidos/', post_pedidos),

    # pedidos
    path('pedidos/<int:id_pedido>/', delete_pedidos),
    path('pedidos/<int:id_pedido>/produtos/', post_pedidosprodutos),

    # pedidosprodutos
    path('estadospedidosprodutos/', get_estadospedidosprodutos),
    path('pedidosprodutos/<int:id_pedido_produto>/', update_delete_pedidosprodutos),
    path('pedidosprodutos/<int:id_pedido_produto>/escolher/', escolher_pedidosprodutos),
    path('pedidosprodutos/<int:id_pedido_produto>/confecionar/', confecionar_pedidosprodutos),

    # estados reservas
    path('estadosreservas/', get_estadosreservas),

    # reservas
    path('reservas/', get_post_reservas),
    path('reservas/<int:id_reserva>/', update_delete_reservas),
    path('reservas/confirmadas/', get_reservas_confirmadas),
    path('reservas/canceladas/', get_reservas_canceladas),
    path('reservas/concluidas/', get_reservas_concluidas),
    path('reservas/<int:id_reserva>/servicos/', post_servico_com_reserva),
    path('reservas/<int:id_reserva>/cancelar/', cancelar_reservas),
    path('reservas/data/', get_reservas_by_data),
]
