from rest_framework.permissions import BasePermission

class BloquearUtilizadoresNaoAutenticados(BasePermission):

    rotas_abertas = [
        '/autenticacao/login/',
        '/autenticacao/signup/',
    ]

    def has_permission(self, request, view):
        # Permitir o acesso a rotas abertas
        print(request.user)
        if request.path in self.rotas_abertas:
            return True

        # Permite o acesso a utilizadores autenticados
        return str(request.user) != 'AnonymousUser'
