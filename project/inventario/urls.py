from django.urls import path
from . import views

urlpatterns = [
    # Ingredientes
    path('ingredientes/', views.get_post_ingredientes),
    path('ingredientes/<str:id_ingrediente>', views.update_delete_ingredientes),
    path('ingredientes/<str:id_ingrediente>/receitas/', views.get_post_ingredientesReceitas),

    # Utensilios
    path('utensilios/', views.get_post_utensilios),
    path('utensilios/<str:id_utensilio>/', views.update_delete_utensilios),
    path('utensilios/<str:id_utensilio>/receitas/', views.get_post_utensiliosReceitas),

    # Fornecedores
    path('fornecedores/', views.get_post_fornecedores),
    path('fornecedores/<str:id_fornecedor>/', views.update_delete_fornecedores),
    path('fornecedores/<str:id_fornecedor>/ingredientes/', views.get_ingredientes_by_fornecedor),
    path('fornecedores/<str:id_fornecedor>/utensilios/', views.get_utensilios_by_fornecedor),

    # Carrinhos
    path('carrinhos/', views.get_carrinhos),
    path('carrinhos/atual/', views.get_carrinho_atual),

    # IngredientesCarrinhos
    path('carrinhos/atual/ingredientes/', views.get_post_ingredientesCarrinhos_atual),
    path('carrinhos/atual/ingredientes/comprar/', views.comprar_carrinho_atual_ingredientes),
    path('carrinhos/<str:id_carrinho>/ingredientes/', views.get_ingredientesCarrinhos),
    path('ingredientescarrinhos/<str:id_ingrediente_carrinho>/', views.update_delete_ingredientesCarrinhos_atual),

    # UtensiliosCarrinhos
    path('carrinhos/atual/utensilios/', views.get_post_utensiliosCarrinhos_atual),
    path('carrinhos/atual/utensilios/comprar/', views.comprar_carrinho_atual_utensilios),
    path('carrinhos/<str:id_carrinho>/utensilios/', views.get_utensiliosCarrinhos),
    path('utensilioscarrinhos/<str:id_utensilio_carrinho>/', views.update_delete_utensiliosCarrinhos_atual),

    # Receitas
    path('receitas/', views.get_post_receitas),
    path('receitas/<str:id_receita>/', views.update_delete_receitas),
    path('receitas/<str:id_receita>/ingredientes/', views.get_post_receitasIngredientes),
    path('ingredientesreceitas/<str:id_ingrediente_receita>/', views.update_delete_ingredientesReceitas),
    path('receitas/<str:id_receita>/utensilios/', views.get_post_receitasUtensilios),
    path('utensiliosreceitas/<str:id_utensilio_receita>/', views.update_delete_utensiliosReceitas),
    path('receitas/<str:id_receita>/instrucoes/', views.get_post_instrucoes),
    path('instrucoes/<str:id_instrucao>/', views.update_delete_instrucoes),
]
