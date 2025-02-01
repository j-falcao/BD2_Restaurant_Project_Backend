from django.urls import path
from . import views

urlpatterns = [
    # Ingredientes
    path('ingredientes/', views.get_post_ingredientes),
    path('ingredientes/<str:id_ingrediente>', views.update_delete_ingredientes),

    # Utensilios
    path('utensilios/', views.get_post_utensilios),
    path('utensilios/<str:id_utensilio>/', views.update_delete_utensilios),

    # Fornecedores
    path('fornecedores/', views.get_post_fornecedores),
    path('fornecedores/<str:id_fornecedor>/', views.update_delete_fornecedores),

    # Carrinhos
    path('carrinhos/', views.get_carrinhos),
    path('carrinhos/<str:id_carrinho>/ingredientes/', views.get_post_ingredientesCarrinhos),
    path('ingredientescarrinhos/<str:id_ingrediente_carrinho>/', views.update_delete_ingredientesCarrinhos),
    path('carrinhos/<str:id_carrinho>/utensilios/', views.get_post_utensiliosCarrinhos),
    path('utensilioscarrinhos/<str:id_utensilio_carrinho>/', views.update_delete_utensiliosCarrinhos),

    # Receitas
    path('receitas/', views.get_post_receitas),
    path('receitas/<str:id_receita>/', views.update_delete_receitas),
    path('receitas/<str:id_receita>/ingredientes/', views.get_post_ingredientesReceitas),
    path('ingredientesreceitas/<str:id_ingrediente_receita>/', views.update_delete_ingredientesReceitas),
    path('receitas/<str:id_receita>/utensilios/', views.get_post_utensiliosReceitas),
    path('utensiliosreceitas/<str:id_utensilio_receita>/', views.update_delete_utensiliosReceitas),
    path('receitas/<str:id_receita>/instrucoes/', views.get_post_instrucoes),
    path('instrucoes/<str:id_instrucao>/', views.update_delete_instrucoes),
]
