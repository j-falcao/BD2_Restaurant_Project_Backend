from rest_framework import serializers
from .models import *

class EstadoMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoMesa
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProduto
        fields = '__all__'


class PedidoProdutoOpcaoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProdutoItemOpcao
        fields = '__all__'
