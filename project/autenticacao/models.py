from django.db import models

class Permissoes(models.Model):
    id_permissao = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissoes'


class Cargos(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos' 


class PermissoesCargos(models.Model):
    id_permissao_cargo = models.AutoField(primary_key=True)
    id_permissao = models.ForeignKey(Permissoes, on_delete=models.CASCADE, db_column='id_permissao')
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, db_column='id_cargo')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissoescargos'


class Utilizadores(models.Model):
    id_utilizador = models.AutoField(primary_key=True)
    cargos = models.ManyToManyField(Cargos, through='UtilizadoresCargos', related_name='utilizadores')
    permissoes = models.ManyToManyField(Permissoes, through='UtilizadoresPermissoes', related_name='utilizadores')
    username = models.CharField(max_length=50, unique=True)
    turno_almoco = models.BooleanField(default=False)
    turno_jantar = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    telemovel = models.CharField(max_length=50, null=True, blank=True, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, null=True, blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    password_hash = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        db_table = 'utilizadores'

    def __str__(self):
        return f"{self.first_name} {self.first_name}"
    

class UtilizadoresCargos(models.Model):
    id_utilizador_cargo = models.AutoField(primary_key=True)
    id_utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_utilizador')
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, db_column='id_cargo')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadorescargos'


class UtilizadoresPermissoes(models.Model):
    id_utilizador_permissao = models.AutoField(primary_key=True)
    id_utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_utilizador')    
    id_permissao = models.ForeignKey(Permissoes, on_delete=models.CASCADE, db_column='id_permissao')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)  

    class Meta:
        managed = False
        db_table = 'utilizadorespermissoes'
