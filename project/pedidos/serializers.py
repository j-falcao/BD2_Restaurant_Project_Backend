from rest_framework import serializers
from .models import *


class EstadosMesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadosMesas
        fields = '__all__'


class MesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'


class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'


class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'


class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


class PedidosProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosProdutos
        fields = '__all__'


class PedidosProdutosOpcoesItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosProdutosItensOpcoes
        fields = '__all__'
