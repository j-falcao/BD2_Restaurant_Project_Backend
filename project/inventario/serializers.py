from rest_framework import serializers
from .models import *


class CarrinhosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinhos
        fields = '__all__'
        

class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = '__all__'


class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'


class UtensiliosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utensilios
        fields = '__all__'


class InstrucoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrucoes
        fields = '__all__'


class ReceitasSerializer(serializers.ModelSerializer):
    ingredientes = IngredientesSerializer(many=True, read_only=True)
    utensilios = UtensiliosSerializer(many=True, read_only=True)
    instrucoes = InstrucoesSerializer(many=True, read_only=True)

    class Meta:
        model = Receitas
        fields = '__all__'