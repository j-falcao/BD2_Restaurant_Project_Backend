from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.utils import OperationalError

class CargosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cargos'

    def ready(self):
        post_migrate.connect(criar_utilizador_dev, sender=self)


def criar_utilizador_dev(sender, **kwargs):
    from .models import Utilizador
    try:
        if not Utilizador.objects.filter(username='dev').exists():
            Utilizador.objects.create_superuser(
                username='dev',
                password='dev'
            )
            print("Utilizador 'dev' criado.")
        else:
            print("Utilizador 'dev' já existe.")
    except OperationalError:
        print("Erro ao criar utilizador 'dev'.")
