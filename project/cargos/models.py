from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilizador(AbstractUser):
    id = models.AutoField(primary_key=True)
    turno_almoco = models.BooleanField(default=False)
    turno_jantar = models.BooleanField(default=False)
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    morada = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10)
    data_registo = models.DateField(auto_now_add=True)

    cargos = models.ManyToManyField(
        'auth.Group',
        related_name='utilizadores',
        blank=True,
        help_text=('Os grupos aos quais este utilizador pertence. O utilizador receberá todas as permissões '
                   'concedidas a cada grupo ao qual pertence.'),
        verbose_name=('cargos'),
    )

    permissoes = models.ManyToManyField(
        'auth.Permission',
        related_name='utilizadores',
        blank=True,
        help_text=('Permissões específicas para este utilizador.'),
        verbose_name=('permissoes'),
    )
    
    class Meta:
        db_table = 'utilizador'

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"




""" 
class Garcom(models.Model):
    
    #Representa um garçom associado a um utilizador específico.
    
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="garcom")

    class Meta:
        managed = False
        db_table = 'garcom'

    def __str__(self):
        return f"Garçom - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"


class Cozinheiro(models.Model):
    
    #Representa um cozinheiro com especialidades específicas.
    
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="cozinheiro")

    class Meta:
        managed = False
        db_table = 'cozinheiro'

    def __str__(self):
        return f"Cozinheiro - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"


class Administrador(models.Model):

    #Representa um administrador associado a um fornecedor específico.
    
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="administrador")

    class Meta:
        managed = False
        db_table = 'administrador'

    def __str__(self):
        return f"Administrador - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"


class Cliente(models.Model):
    
    #Representa um cliente associado a um utilizador específico.

    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="cliente")

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return f"Cliente - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"
"""