from django.urls import path
from .views import *
from servicos import views as servicos_views

urlpatterns = [
    # autenticacao
    path('login/', login_view),
    path('signup/', signup_view),
    
    # utilizadores
    path('utilizadores/', get_all_utilizadores_view),

    # garcons
    path('garcons/', get_all_garcons_view),
    path('garcons/<int:id_garcon>/servicos/', servicos_views.get_servicos_by_garcom),
    path('garcons/<int:id_garcon>/reservas/', servicos_views.get_reservas_by_garcom),

    # cozinheiros
    path('cozineiros/', get_all_cozinheiros_view),
    
    # administradores
    path('administradores/', get_all_administradores_view),
    path('superusers/', get_all_superusers_view),

    # debug
    path('mee_bd/', mee_bd_view), 
]
