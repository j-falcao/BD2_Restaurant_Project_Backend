from django.db import models

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=100)
    telemovel = models.CharField(max_length=9)
    email = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_registo = models.DateField(auto_now_add=True)
    tipo_utilizador = models.ForeignKey('TipoUtilizador', on_delete=models.CASCADE, related_name='utilizadores')

    class Meta:
        db_table = 'utilizador'

    def __str__(self):
        return self.nome

class TipoUtilizador(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipo_utilizador'

    def __str__(self):
        return self.descricao

class Turno(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = 'turno'

    def __str__(self):
        return self.descricao
