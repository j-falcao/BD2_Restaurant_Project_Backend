from django.urls import path
from . import views_produtos

urlpatterns = [
    path('produtos/', views_produtos.get_produtos, name='produtos'),
    path('produtos/<int:id_produto>/', views_produtos.get_produto, name='produto'),

    path('itens/', views_produtos.get_itens, name='itens'),
    path('itens/<int:id_item>/', views_produtos.get_item, name='item'),

    path('tipos/', views_produtos.get_tipos, name='tipos'),
    path('tipos/<int:id_tipo>/', views_produtos.get_tipo, name='tipo'),

    path('categorias/', views_produtos.get_categorias, name='categorias'),
    path('categorias/<int:id_categoria>/', views_produtos.get_categoria, name='categoria'),

    path('opcoes/', views_produtos.get_opcoes, name='opcoes'),
    path('opcoes/<int:id_opcao>/', views_produtos.get_opcao, name='opcao'),

    path('menus/', views_produtos.get_menus, name='menus'),
    path('menus/<int:id_menu>/', views_produtos.get_menu, name='menu'),
]
