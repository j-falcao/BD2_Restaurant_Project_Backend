from rest_framework import serializers
from .models import *
from .db import *

class IngredientesSerializer(serializers.ModelSerializer): #✅
    id_fornecedor = serializers.IntegerField()

    class Meta:
        model = Ingredientes
        fields = '__all__'

    def create(self, validated_data):
        return get_ingredientes(create_ingredientes(validated_data))
    
    def update(self, instance, validated_data):
        update_ingredientes(instance.id_ingrediente, validated_data)
        return get_ingredientes(instance.id_ingrediente)

class UtensiliosSerializer(serializers.ModelSerializer): #✅
    class Meta:
        model = Utensilios
        fields = '__all__'

    def create(self, validated_data):
        return get_utensilios(create_utensilios(validated_data))
    
    def update(self, instance, validated_data):
        update_utensilios(instance.id_utensilio, validated_data)
        return get_utensilios(instance.id_utensilio)
    
class FornecedoresSerializer(serializers.ModelSerializer):  #✅
    class Meta:
        model = Fornecedores
        fields = '__all__'

    def create(self, validated_data):
        return get_fornecedores(create_fornecedores(validated_data))
    
    def update(self, instance, validated_data):
        update_fornecedores(instance.id_fornecedor, validated_data)
        return get_fornecedores(instance.id_fornecedor)


class CarrinhosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinhos
        fields = '__all__'


class IngredientesCarrinhosSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientesCarrinhos
        fields = '__all__'


class UtensiliosCarrinhosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtensiliosCarrinhos
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

class UtensiliosReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtensiliosReceitas
        fields = '__all__'


class IngredientesReceitasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = IngredientesReceitas
        fields = '__all__'
