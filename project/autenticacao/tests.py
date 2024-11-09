from django.contrib.auth.models import Group
from rest_framework.test import APITestCase, APIClient
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Utilizador

class TesteAutenticacaoUtilizadores(APITestCase):

    def setUp(self):
        # Criação dos grupos
        self.grupo_garcom = Group.objects.create(name="Garçom")
        self.grupo_cozinheiro = Group.objects.create(name="Cozinheiro")
        self.grupo_administrador = Group.objects.create(name="Administrador")

        # Criação dos utilizadores e atribuição dos grupos/cargos
        self.utilizador_garcom = Utilizador.objects.create_user(username="garcom", password="senha_garcom")
        self.utilizador_garcom.cargos.add(self.grupo_garcom)

        self.utilizador_cozinheiro = Utilizador.objects.create_user(username="cozinheiro", password="senha_cozinheiro")
        self.utilizador_cozinheiro.cargos.add(self.grupo_cozinheiro)

        self.utilizador_administrador = Utilizador.objects.create_user(username="administrador", password="senha_admin")
        self.utilizador_administrador.cargos.add(self.grupo_administrador)

    def test_utilizador_pode_pertencer_a_apenas_um_grupo(self):
        # Testa se um utilizador pode pertencer a apenas um grupo
        novo_utilizador = Utilizador.objects.create_user(username="novoutilizador", password="senha_novo")
        novo_utilizador.groups.add(self.grupo_garcom)

        # Tentativa de adicionar o utilizador a outro grupo deve falhar
        with self.assertRaises(ValidationError):
            novo_utilizador.groups.add(self.grupo_cozinheiro)
            novo_utilizador.clean()  # Executa a validação

    def test_autenticacao_garcom(self):
        # Teste de autenticação para Garçom
        client = APIClient()
        resposta = client.post(reverse('token_obtain_pair'), {'username': 'garcom', 'password': 'senha_garcom'})
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("access", resposta.data)

    def test_autenticacao_cozinheiro(self):
        # Teste de autenticação para Cozinheiro
        client = APIClient()
        resposta = client.post(reverse('token_obtain_pair'), {'username': 'cozinheiro', 'password': 'senha_cozinheiro'})
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("access", resposta.data)

    def test_autenticacao_cliente(self):
        # Teste de autenticação para Cliente
        client = APIClient()
        resposta = client.post(reverse('token_obtain_pair'), {'username': 'cliente', 'password': 'senha_cliente'})
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("access", resposta.data)

    def test_autenticacao_administrador(self):
        # Teste de autenticação para Administrador
        client = APIClient()
        resposta = client.post(reverse('token_obtain_pair'), {'username': 'administrador', 'password': 'senha_admin'})
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("access", resposta.data)

    def test_credenciais_invalidas(self):
        # Teste de autenticação com credenciais inválidas
        client = APIClient()
        resposta = client.post(reverse('token_obtain_pair'), {'username': 'garcom', 'password': 'senha_errada'})
        self.assertEqual(resposta.status_code, 401)
        self.assertIn("detail", resposta.data)

    def test_utilizador_nao_pode_pertencer_a_varios_grupos(self):
        # Testa a restrição para evitar que um utilizador pertença a múltiplos grupos
        utilizador = Utilizador.objects.create_user(username="testeutilizador", password="senha_teste")
        utilizador.groups.add(self.grupo_garcom)

        # Tentativa de adicionar o utilizador a outro grupo deve gerar uma exceção de validação
        with self.assertRaises(ValidationError):
            utilizador.groups.add(self.grupo_cozinheiro)
            utilizador.clean()

    def test_apenas_um_grupo_atribuido(self):
        # Testa se o utilizador está associado a apenas um grupo após validação
        utilizador = Utilizador.objects.create_user(username="utilizadorunico", password="senha_unica")
        utilizador.groups.add(self.grupo_cliente)

        # Verifica se o utilizador está realmente em apenas um grupo
        self.assertEqual(utilizador.groups.count(), 1)

        # Tenta atribuir outro grupo e captura a exceção
        with self.assertRaises(ValidationError):
            utilizador.groups.add(self.grupo_administrador)
            utilizador.clean()
        self.assertEqual(utilizador.groups.count(), 1)  # Verifica se não houve adição indevida
