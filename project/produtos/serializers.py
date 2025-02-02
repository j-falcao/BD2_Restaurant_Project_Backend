""" from rest_framework import serializers
from .models import *

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'


class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = '__all__'


class TiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos
        fields = '__all__'


class ItensTiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensTipos
        fields = '__all__'


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ItensCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCategorias
        fields = '__all__'


class OpcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcoes
        fields = '__all__'


class ItensOpcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensOpcoes
        fields = '__all__'


class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'


class MenusItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensMenus
        fields = '__all__'


class DiasSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiasSemana
        fields = '__all__'


class MenusDiasSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenusDiasSemana
        fields = '__all__'
 """