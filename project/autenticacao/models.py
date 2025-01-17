from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class Cargos(models.Model):
    id_cargo = models.AutoField(primary_key=True, unique=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos_view'

    def __str__(self):
        return self.designacao

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field is required')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)

class Utilizadores(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    is_superuser = models.BooleanField(default=False)
    cargos = models.ManyToManyField(Cargos, through='UtilizadoresCargos')
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'utilizadores_view'

    def __str__(self):
        return self.username

class UtilizadoresCargos(models.Model):
    id_utilizador_cargo = models.AutoField(primary_key=True, unique=True)
    id_utilizador = models.ForeignKey(
        Utilizadores,
        on_delete=models.CASCADE,
        db_column='id_utilizador'
    )
    id_cargo = models.ForeignKey(
        Cargos,
        on_delete=models.CASCADE,
        db_column='id_cargo'
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadorescargos_view'

    def __str__(self):
        return f"{self.id_utilizador} - {self.id_cargo}"
