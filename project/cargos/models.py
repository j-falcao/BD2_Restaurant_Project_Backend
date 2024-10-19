from django.db import models
from django.contrib.auth.models import AbstractUser

class TipoUtilizador(models.Model):
    id_tipo_utilizador = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False

    def __str__(self):
        return self.descricao


class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    class Meta:
        managed = False

    def __str__(self):
        return self.nome


class Utilizador(AbstractUser):
    id_utilizador = models.AutoField(primary_key=True)
    tipo_utilizador = models.ForeignKey(TipoUtilizador, on_delete=models.CASCADE, related_name="utilizadores")
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
        managed = False

    # Correção: Os campos groups e user_permissions precisam estar dentro da classe
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='cargos_utilizador_groups',  # Adiciona related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='cargos_utilizador_user_permissions',  # Adiciona related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"


class Garcom(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="garcom")

    class Meta:
        managed = False

    def __str__(self):
        return f"Garçom - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"
    

class GarcomIdioma(models.Model):
    id_garcom_idioma = models.AutoField(primary_key=True)
    garcom = models.ForeignKey(Garcom, on_delete=models.CASCADE, related_name="idiomas")
    idioma = models.CharField(max_length=50)

    class Meta:
        managed = False

    def __str__(self):
        return f"{self.garcom.utilizador.primeiro_nome} {self.garcom.utilizador.ultimo_nome} - {self.idioma}"


class Cozinheiro(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="cozinheiro")
    especialidades = models.CharField(max_length=255)

    class Meta:
        managed = False

    def __str__(self):
        return f"Cozinheiro - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"


class Administrador(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="administrador")
    fornecedor = models.ForeignKey('inventario.Fornecedor', on_delete=models.DO_NOTHING, related_name="administradores")

    class Meta:
        managed = False

    def __str__(self):
        return f"Administrador - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"
    

class Cliente(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True, related_name="cliente")

    class Meta:
        managed = False

    def __str__(self):
        return f"Cliente - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"
