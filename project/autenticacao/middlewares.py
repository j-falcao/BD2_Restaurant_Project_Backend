from django.utils.deprecation import MiddlewareMixin
from threading import local
from autenticacao.auth import CookieJWTAuthentication

_thread_local = local()

_user_db_mapping = {
    'Garcom': 'garcom',
    'Cozinheiro': 'cozinheiro',
    'Administrador': 'administrador',
}

def get_current_db():
    return getattr(_thread_local, 'db', 'default')

def set_current_db(db_alias):
    _thread_local.db = db_alias

class DynamicDatabaseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/estatisticas/'):
            set_current_db('mongo')
            return
        
        utilizador, _ = CookieJWTAuthentication().authenticate(request) or (None, None)
        if not utilizador:
            set_current_db('default')
            return
        
        if utilizador['is_superuser']:
            set_current_db('default')
            return
        
        cargo = utilizador['cargo']['designacao']
        
        if cargo in _user_db_mapping:
            set_current_db(_user_db_mapping[cargo])
        else:
            set_current_db('default')
    
    def process_response(self, request, response):
        set_current_db('default')
        return response

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        return get_current_db()

    def db_for_write(self, model, **hints):
        return get_current_db()

    def allow_relation(self, obj1, obj2, **hints):
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return False
