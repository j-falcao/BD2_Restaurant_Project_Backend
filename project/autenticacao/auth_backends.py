from django.contrib.auth.backends import BaseBackend
from django.db import connection
from django.contrib.auth.hashers import check_password
from .models import Utilizadores

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_utilizador, password FROM utilizadores WHERE username = %s", [username])
            row = cursor.fetchone()
            if row and check_password(password, row[1]):
                return Utilizadores(id_utilizador=row[0], username=username)

        return None
