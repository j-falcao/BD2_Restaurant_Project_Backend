from django.db import models
from project.utils.db_utils import fetch_from_view

class Cargos(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos'

    def __str__(self):
        return self.designacao
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("cargos_view")

class Utilizadores(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, db_column='id_cargo')
    url_imagem = models.CharField(max_length=2048, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'utilizadores'
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("utilizadores_view")
    
    @staticmethod
    def fetch_by_id(id_utilizador):
        return fetch_from_view("utilizadores_view", {"id_utilizador": id_utilizador})
    
    @staticmethod
    def fetch_all_garcons():
        return fetch_from_view("garcons_view")
    
    @staticmethod
    def fetch_all_administradores():
        return fetch_from_view("administradores_view")
    
    @staticmethod
    def fetch_all_cozinheiros():
        return fetch_from_view("cozinheiros_view")
    
    @staticmethod
    def fetch_all_superusers():
        return fetch_from_view("superusers_view")
    
    @staticmethod
    def fetch_by_username(username):
        return fetch_from_view("utilizadores_view", {"username": username})
    
    @staticmethod
    def fetch_utilizadores_by_cargo(id_cargo):
        return fetch_from_view("utilizadorescargos_view", {"id_cargo": id_cargo})

    @staticmethod
    def fetch_cargos_by_utilizador(id_utilizador):
        return fetch_from_view("utilizadorescargos_view", {"id_utilizador": id_utilizador})


# class UtilizadoresCargos(models.Model):
#     id_utilizador_cargo = models.AutoField(primary_key=True)
#     id_utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_utilizador')
#     id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, db_column='id_cargo')
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'utilizadorescargos'

#     def __str__(self):
#         return f"{self.id_utilizador} - {self.id_cargo}"
    
#     @staticmethod
#     def fetch_all():
#         return fetch_from_view("utilizadorescargos_view")
    
