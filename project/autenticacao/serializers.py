from rest_framework import serializers
from .models import Cargos, Utilizadores, UtilizadoresCargos


class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = '__all__'


class UtilizadoresSerializer(serializers.ModelSerializer):
    cargos = CargosSerializer(many=True, read_only=True)

    class Meta:
        model = Utilizadores
        fields = '__all__'        


class UtilizadoresCargosSerializer(serializers.ModelSerializer):
    id_utilizador = UtilizadoresSerializer(read_only=True)
    id_cargo = CargosSerializer(read_only=True)

    class Meta:
        model = UtilizadoresCargos
        fields = '__all__'
