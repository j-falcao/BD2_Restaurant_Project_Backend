from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

class Turno(models.Model):
    
    #Representa um turno de trabalho com nome, hora de início e fim.
    
    id_turno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    class Meta:
        managed = False
        db_table = 'turno'

    def __str__(self):
        return self.nome


class Utilizador(AbstractUser):
    
    #Classe de utilizador estendida com informações adicionais como tipo, turno e dados pessoais.
    
    id = models.AutoField(primary_key=True)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="utilizadores")
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    morada = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)
    data_registo = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'utilizador'

    cargo = models.ManyToManyField(
        'auth.Group',
        related_name='utilizadores',
        blank=True,
        help_text=('Os grupos aos quais este utilizador pertence. O utilizador receberá todas as permissões '
                   'concedidas a cada grupo ao qual pertence.'),
        verbose_name=('grupos'),
    )

    permissoes = models.ManyToManyField(
        'auth.Permission',
        related_name='utilizadores',
        blank=True,
        help_text=('Permissões específicas para este utilizador.'),
        verbose_name=('permissoes'),
    )
    
    def clean(self):
        super().clean()
        # Verifica se o utilizador está associado a mais de um grupo
        if self.groups.count() > 1:
            raise ValidationError("Um utilizador pode pertencer a apenas um grupo/cargo.")

    def save(self, *args, **kwargs):
        # Chama o método clean antes de salvar o utilizador
        self.clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"








""" class Garcom(models.Model):
    
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