from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('utilizadores/', get_all_utilizadores_view, name='get_all_utilizadores'),
    path('utilizador/username/<str:username>/', get_utilizador_by_username_view, name='get_utilizador_by_username'),
    path('utilizador/id/<int:id_utilizador>/', get_utilizador_by_id_view, name='get_utilizador_by_id'),
    path('utilizador/email/<str:email>/', get_utilizador_by_email_view, name='get_utilizador_by_email'),
    path('utilizador/telemovel/<str:telemovel>/', get_utilizador_by_telemovel_view, name='get_utilizador_by_telemovel'),
    path('utilizadores/cozinheiros/', get_all_cozinheiros_view, name='get_all_cozinheiros'),
    path('utilizadores/garcons/', get_all_garcons_view, name='get_all_garcons'),
    path('utilizadores/administradores/', get_all_administradores_view, name='get_all_administradores'),
    path('cargos/', get_all_cargos_view, name='get_all_cargos'),
    path('cargo/id/<int:id_cargo>/', get_cargo_by_id_view, name='get_cargo_by_id'),
    path('cargo/designacao/<str:designacao>/', get_cargo_by_designacao_view, name='get_cargo_by_designacao'),
    path('utilizadores_cargos/', get_all_utilizadores_cargos_view, name='get_all_utilizadores_cargos'),
    path('utilizadores_cargos/utilizador/<int:id_utilizador>/', get_utilizadores_cargos_by_id_utilizador_view, name='get_utilizadores_cargos_by_id_utilizador'),
    path('utilizadores_cargos/cargo/<int:id_cargo>/', get_utilizadores_cargos_by_id_cargo_view, name='get_utilizadores_cargos_by_id_cargo'),
]
