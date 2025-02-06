from django.urls import path
from .views import *

urlpatterns = [
    path('estadosmesas/', get_post_estados_mesas),
    path('estadosmesas/<int:id_estado_mesa>/', update_delete_estados_mesas),

    path('mesas/', get_post_mesas),
    path('mesas/<int:id_mesa>/', update_delete_mesas),

    path('', get_post_servicos),
    path('<int:id_servico>/', update_delete_servicos),
    path('<int:id_servico>/concluir/', concluir_servicos),
    path('<int:id_servico>/pedidos/', get_post_pedidos),
    path('pedidos/<int:id_pedido>/', delete_pedidos),
    path('pedidos/<int:id_pedido>/produtos/', get_post_pedidosProdutos),
    path('pedidosprodutos/<int:id_pedido_produto>/', delete_pedidosProdutos),
    path('pedidosprodutos/<int:id_pedido_produto>/confecionar/', confecionar_pedidosProdutos),

    path('reservas/', get_post_reservas),
    path('reservas/<int:id_reserva>/', update_delete_reservas),
    path('reservas/<int:id_reserva>/servicos/', post_servico_com_reserva),
    path('reservas/<int:id_reserva>/cancelar/', cancelar_reservas),

]
