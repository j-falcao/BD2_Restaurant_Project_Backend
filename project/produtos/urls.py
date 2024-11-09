from django.urls import path
from .views import *

urlpatterns = [
    path('produtos/', get_produtos, name='produtos'),
    path('produtos/<int:id_produto>/', get_produto, name='produto'),

    path('itens/', get_itens, name='itens'),
    path('itens/<int:id_item>/', get_item, name='item'),

    path('tipos/', get_tipos, name='tipos'),
    path('tipos/<int:id_tipo>/', get_tipo, name='tipo'),

    path('categorias/', get_categorias, name='categorias'),
    path('categorias/<int:id_categoria>/', get_categoria, name='categoria'),

    path('opcoes/', get_opcoes, name='opcoes'),
    path('opcoes/<int:id_opcao>/', get_opcao, name='opcao'),

    path('menus/', get_menus, name='menus'),
    path('menus/<int:id_menu>/', get_menu, name='menu'),
]
