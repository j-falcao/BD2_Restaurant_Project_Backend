from rest_framework import serializers
from .models import (
    Produto, Item, Tipo, ItemTipo, Categoria, ItemCategoria, 
    Opcao, ItemOpcao, Menu, ItemMenu, DiaSemana, MenuDiaSemana
)

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'


class ItemTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipo
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ItemCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategoria
        fields = '__all__'


class OpcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcao
        fields = '__all__'


class ItemOpcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOpcao
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMenu
        fields = '__all__'


class DiaSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaSemana
        fields = '__all__'


class MenuDiaSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuDiaSemana
        fields = '__all__'
