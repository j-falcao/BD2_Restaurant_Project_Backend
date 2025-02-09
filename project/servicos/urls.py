from django.urls import path
from .views import *

urlpatterns = [
    # estados mesas
    path('estadosmesas/', get_post_estadosmesas),
    path('estadosmesas/<int:id_estado_mesa>/', update_delete_estadosmesas),

    # mesas
    path('mesas/', get_post_mesas),
    path('mesas/<int:id_mesa>/', update_delete_mesas),
    path('mesas/disponiveis/', get_mesas_disponiveis),
    path('mesas/ocupadas/', get_mesas_ocupadas),
    path('mesas/reservadas/', get_mesas_reservadas),
    

    # servicos
    path('', get_post_servicos),
    path('<int:id_servico>/', update_delete_servicos),
    path('<int:id_servico>/concluir/', concluir_servicos),
    path('<int:id_servico>/pedidos/', get_post_pedidos),

    # pedidos
    path('pedidos/<int:id_pedido>/', delete_pedidos),
    path('pedidos/<int:id_pedido>/produtos/', get_post_pedidosProdutos),

    # pedidosprodutos
    path('pedidosprodutos/<int:id_pedido_produto>/', delete_pedidosProdutos),
    path('pedidosprodutos/<int:id_pedido_produto>/confecionar/',
         confecionar_pedidosProdutos),

    # estados reservas
    path('estadosreservas/', get_post_estadosreservas),
    path('estadosreservas/<int:id_estado_reserva>/', update_delete_estadosreservas),

    # reservas
    path('reservas/', get_post_reservas),
    path('reservas/confirmadas/', get_reservas_confirmadas),
    path('reservas/canceladas/', get_reservas_canceladas),
    path('reservas/concluidas/', get_reservas_concluidas),
    path('reservas/<int:id_reserva>/', update_delete_reservas),
    path('reservas/<int:id_reserva>/servicos/', post_servico_com_reserva),
    path('reservas/<int:id_reserva>/cancelar/', cancelar_reservas),

]
