from django.urls import path
from . import views_pedidos

urlpatterns = [
    path('estados_mesa/', views_pedidos.get_estados_mesa, name='estados_mesa'),
    path('estados_mesa/<int:id_estado_mesa>/', views_pedidos.get_estado_mesa, name='estado_mesa'),

    path('mesas/', views_pedidos.get_mesas, name='mesas'),
    path('mesas/<int:id_mesa>/', views_pedidos.get_mesa, name='mesa'),

    path('servicos/', views_pedidos.get_servicos, name='servicos'),
    path('servicos/<int:id_servico>/', views_pedidos.get_servico, name='servico'),

    path('reservas/', views_pedidos.get_reservas, name='reservas'),
    path('reservas/<int:id_reserva>/', views_pedidos.get_reserva, name='reserva'),

    path('pedidos/', views_pedidos.get_pedidos, name='pedidos'),
    path('pedidos/<int:id_pedido>/', views_pedidos.get_pedido, name='pedido'),
]
