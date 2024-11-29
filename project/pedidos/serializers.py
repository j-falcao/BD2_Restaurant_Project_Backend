from rest_framework import serializers
from .models import *


class EstadoMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoMesa
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


class PedidoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosProdutos
        fields = '__all__'


class PedidoProdutoOpcaoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosProdutosItensOpcoes
        fields = '__all__'
