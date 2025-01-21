from django.urls import path
from . import views

urlpatterns = [
    path('ingredientes/', views.get_post_ingredientes, name='ingredientes'),
    path('ingredientes/<str:id_ingrediente>', views.update_delete_ingredientes, name='ingrediente'),

    path('utensilios/', views.get_post_utensilios, name='utensilios'),
    path('utensilios/<str:id_utensilio>/', views.update_delete_utensilios, name='utensilio'),

    path('fornecedores/', views.get_post_fornecedores, name='fornecedores'),
    path('fornecedores/<str:id_fornecedor>/', views.update_delete_fornecedores, name='fornecedor'),

    path('carrinhos/', views.get_carrinhos, name='carrinhos'),

    path('ingredientescarrinhos/', views.get_post_ingredientesCarrinhos, name='ingredientescarrinhos'),
    path('ingredientescarrinhos/<str:id_ingredientescarrinho>/', views.update_delete_ingredientesCarrinhos, name='ingredientescarrinho'),

    path('utensilioscarrinhos/', views.get_post_utensiliosCarrinhos, name='utensilioscarrinhos'),
    path('utensilioscarrinhos/<str:id_utensilioscarrinho>/', views.update_delete_utensiliosCarrinhos, name='utensilioscarrinho'),

    path('receitas/', views.get_post_receitas, name='receitas'),
    path('receitas/<str:id_receita>/', views.update_delete_receitas, name='receita'),

    path('ingredientesreceitas/', views.get_post_ingredientesReceitas, name='ingredientesreceitas'),
    path('ingredientesreceitas/<str:id_ingredientesreceita>/', views.update_delete_ingredientesReceitas, name='ingredientesreceita'),

    path('utensiliosreceitas/', views.get_post_utensiliosReceitas, name='utensiliosreceitas'),
    path('utensiliosreceitas/<str:id_utensiliosreceita>/', views.update_delete_utensiliosReceitas, name='utensiliosreceita'),

    path('instrucoes/', views.get_post_instrucoes, name='instrucoes'),
    path('instrucoes/<str:id_instrucao>/', views.update_delete_instrucoes, name='instrucao'),
]
