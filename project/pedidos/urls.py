from django.urls import path
from .views import *

urlpatterns = [
    path('estados_mesa/', get_estados_mesa, name='estados_mesa'),
    path('estados_mesa/<int:id_estado_mesa>/', get_estado_mesa, name='estado_mesa'),

    path('mesas/', get_mesas, name='mesas'),
    path('mesas/<int:id_mesa>/', get_mesa, name='mesa'),

    path('servicos/', get_servicos, name='servicos'),
    path('servicos/<int:id_servico>/', get_servico, name='servico'),

    path('reservas/', get_reservas, name='reservas'),
    path('reservas/<int:id_reserva>/', get_reserva, name='reserva'),

    path('pedidos/', get_pedidos, name='pedidos'),
    path('pedidos/<int:id_pedido>/', get_pedido, name='pedido'),
]
