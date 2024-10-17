from django.db import models
from django.contrib.auth.models import AbstractUser

class TipoUtilizador(models.Model):
    id_tipo_utilizador = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return self.nome


class Utilizador(AbstractUser):
    id_utilizador = models.AutoField(primary_key=True)
    tipo_utilizador = models.ForeignKey(TipoUtilizador, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    morada = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)
    data_registo = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
    

class Garcom(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Garçom - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"
    

class GarcomIdioma(models.Model):
    id_garcom_idioma = models.AutoField(primary_key=True)
    garcom = models.ForeignKey(Garcom, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.garcom.utilizador.primeiro_nome} {self.garcom.utilizador.ultimo_nome} - {self.idioma}"


class Cozinheiro(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True)
    especialidades = models.CharField(max_length=255)

    def __str__(self):
        return f"Cozinheiro - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"


class Administrador(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True)
    fornecedor = models.ForeignKey('inventario.Fornecedor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Administrador - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"
    
class Cliente(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Cliente - {self.utilizador.primeiro_nome} {self.utilizador.ultimo_nome}"