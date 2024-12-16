from django.urls import path
from . import views

urlpatterns = [
    path('ingredientes/', views.get_post_ingredientes, name='ingredientes'),
    path('ingredientes/<str:id_ingrediente>', views.update_delete_ingredientes, name='ingrediente'),

    path('utensilios/', views.get_utensilios, name='utensilios'),
    path('utensilios/<str:id_utensilio>/', views.get_utensilio, name='utensilio'),

    path('receitas/', views.get_receitas, name='receitas'),
    path('receitas/<str:id_receita>/', views.get_receita, name='receita'),

    path('carrinhos/', views.get_carrinhos, name='carrinhos'),
    path('carrinhos/<str:id_carrinho>/', views.get_carrinho, name='carrinho'),

    path('fornecedores/', views.get_fornecedores, name='fornecedores'),
    path('fornecedores/<str:id_fornecedor>/', views.get_fornecedor, name='fornecedor'),
]
