from django.urls import path
from .views import *

urlpatterns = [
    # Tipos
    path('tipos/', get_post_tipos),
    path('tipos/<int:id_tipo>/', update_delete_tipos),
    path('tipos/<int:id_tipo>/itens', get_itens_by_tipo),

    # Categorias
    path('categorias/', get_post_categorias),
    path('categorias/<int:id_categoria>/', update_delete_categorias),
    path('categorias/<int:id_categoria>/itens', get_itens_by_categoria),

    # Opcoes
    path('opcoes/', get_post_opcoes),
    path('opcoes/<int:id_opcao>/', update_delete_opcoes),
    path('opcoes/<int:id_opcao>/itens', get_itens_by_opcao),

    # Itens
    path('itens/', get_post_itens),
    path('itens/<int:id_item>/', update_delete_itens),

    path('itens/<int:id_item>/opcoes', get_post_itensOpcoes),
    path('itensopcoes/<int:id_item_opcao>/', delete_itensOpcoes),

    path('itens/<int:id_item>/tipos', get_post_itensTipos),
    path('itenstipos/<int:id_item_tipo>/', delete_itensTipos),

    path('itens/<int:id_item>/categorias', get_post_itensCategorias),
    path('itenscategorias/<int:id_item_categoria>/', delete_itensCategorias),

    path('itens/<int:id_item>/menus', get_menus_by_item),
    
    # Menus
    path('menus/', get_post_menus),
    path('menus/<int:id_menu>/', update_delete_menus),

    path('menus/<int:id_menu>/itens', get_post_itensMenus),
    path('itensmenus/<int:id_item_menu>/', update_delete_itensMenus),

    path('menus/<int:id_menu>/diassemana/', get_post_menusDiasSemana),
    path('menusdiassemana/<int:id_menu_dia_semana>/', update_delete_menusDiasSemana),

    path('diassemana/<int:id_dia_semana>/menus', get_menus_by_diasemana),

]
