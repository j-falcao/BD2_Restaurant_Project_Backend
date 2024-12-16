from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.utils import OperationalError

class AutenticacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autenticacao'
