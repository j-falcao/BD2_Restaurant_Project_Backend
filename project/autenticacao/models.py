from django.db import models
from project.utils.db_utils import fetch_from_view

class Cargos(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos_view'

    def __str__(self):
        return self.designacao
    
    @staticmethod
    def fetch_by_id(id_cargo):
        return fetch_from_view("cargos_view", {"id_cargo": id_cargo})[0]
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("cargos_view")

class Utilizadores(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, db_column='id_cargo')
    url_imagem = models.CharField(max_length=2048, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'Utilizador: {self.id} - {self.first_name} {self.last_name} - Username: {self.username}'

    class Meta:
        managed = False
        db_table = 'utilizadores_view'
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("utilizadores_view")
    
    @staticmethod
    def fetch_by_id(id_utilizador):
        return fetch_from_view("utilizadores_view", {"id": id_utilizador})[0]
    
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
    def fetch_by_username(username):
        return fetch_from_view("utilizadores_view", {"username": username})[0]
    
    @staticmethod
    def fetch_utilizadores_by_cargo(id_cargo):
        return fetch_from_view("utilizadorescargos_view", {"id_cargo": id_cargo})