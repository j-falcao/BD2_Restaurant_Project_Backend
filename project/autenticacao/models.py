from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilizador(AbstractUser):
    id = models.AutoField(primary_key=True)
    turno_almoco = models.BooleanField(default=False)
    turno_jantar = models.BooleanField(default=False)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    

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
        return f"{self.first_name} {self.first_name}"