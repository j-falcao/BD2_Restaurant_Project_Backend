from rest_framework import serializers
from .models import *


class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = '__all__'
        

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class IngredienteCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredienteCarrinho
        fields = '__all__'


class UtensilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utensilio
        fields = '__all__'


class UtensilioCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtensilioCarrinho
        fields = '__all__'


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'


class UtensilioReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtensilioReceita
        fields = '__all__'


class InstrucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrucao
        fields = '__all__'