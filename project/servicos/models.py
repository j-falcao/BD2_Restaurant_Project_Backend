from django.db import connection, models
from autenticacao.models import Utilizadores
from project.utils.db_utils import fetch_from_view
from datetime import datetime


class EstadosMesas(models.Model):
    id_estado_mesa = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadosmesas_view'

    def __str__(self):
        return f"Estado da Mesa - {self.designacao}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("estadosmesas_view")


class Mesas(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    id_estado_mesa = models.ForeignKey(EstadosMesas, on_delete=models.CASCADE, db_column='id_estado_mesa')
    numero = models.IntegerField()
    capacidade_maxima = models.IntegerField()
    quantidade_clientes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesas_view'

    def __str__(self):
        return f"Mesa {self.numero}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("mesas_view")
    
    @staticmethod
    def fetch_disponiveis():
        return fetch_from_view("mesas_disponiveis_view")
    
    @staticmethod
    def fetch_ocupadas():
        return fetch_from_view("mesas_ocupadas_view")
    
    @staticmethod
    def fetch_reservadas():
        return fetch_from_view("mesas_reservadas_view")

class Servicos(models.Model):
    id_servico = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE, db_column='id_mesa')
    id_garcom = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_garcom')
    data_hora_inicio = models.DateTimeField(auto_now_add=True)
    data_hora_fim = models.DateTimeField(null=True, blank=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicos_view'

    def __str__(self):
        return f"Serviço {self.id_servico} na Mesa {self.id_mesa}"
    
    @staticmethod
    def fetch_com_pedidos(id_servico):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM get_servicos_com_pedidos(%s)", [id_servico])
            return cursor.fetchone()[0]

    @staticmethod
    def fetch_all():
        return fetch_from_view("servicos_view")
    
    @staticmethod
    def fetch_by_mesa(id_mesa):
        return fetch_from_view("servicos_view", {"id_mesa": id_mesa})
    
    @staticmethod
    def fetch_by_garcom(id_garcom):
        return fetch_from_view("servicos_view", {"id_garcom": id_garcom})
    
    @staticmethod
    def fetch_ativos():
        return fetch_from_view("servicos_view", {"data_hora_fim": None}) 

    @staticmethod
    def fetch_by_data(data_hora_inicio, data_hora_fim):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_servicos_by_data(%s, %s, %s)", [data_hora_inicio, data_hora_fim, None])
            return cursor.fetchone()[0]


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_servico = models.ForeignKey(Servicos, on_delete=models.CASCADE, db_column='id_servico')
    produtos = models.ManyToManyField('produtos.Produtos', through='PedidosProdutos', related_name='pedidos')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos_view'

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.created_at}"

class EstadosPedidosProdutos(models.Model):
    id_estado_pedido_produto = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadospedidosprodutos_view'

    def __str__(self):
        return f"Estado da Mesa - {self.designacao}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("estadospedidosprodutos_view")


class PedidosProdutos(models.Model):
    id_pedido_produto = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, db_column='id_pedido')
    id_produto = models.ForeignKey('produtos.Produtos', on_delete=models.CASCADE, db_column='id_produto')
    id_estado_pedido_produto = models.ForeignKey(EstadosPedidosProdutos, on_delete=models.CASCADE, db_column='id_estado_pedido_produto')
    quantidade = models.IntegerField()
    id_cozinheiro = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_cozinheiro')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidosprodutos_view'
    

class EstadosReservas(models.Model):
    id_estado_reserva = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadosreservas_view'

    def __str__(self):
        return f"Estado da Reserva - {self.designacao}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("estadosreservas_view")


class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE, db_column='id_mesa')
    id_garcom = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_garcom')
    quantidade_pessoas = models.IntegerField()
    observacoes = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    minutos_antes = models.DurationField()
    minutos_depois = models.DurationField()
    id_servico = models.ForeignKey(Servicos, on_delete=models.CASCADE, db_column='id_servico')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservas_view'

    def __str__(self):
        return f"Reserva {self.id_reserva} na Mesa {self.id_mesa}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("reservas_view")
    
    @staticmethod
    def fetch_confirmadas():
        return fetch_from_view("reservas_confirmadas_view")
    
    @staticmethod
    def fetch_canceladas():
        return fetch_from_view("reservas_canceladas_view")
    
    @staticmethod
    def fetch_concluidas():
        return fetch_from_view("reservas_concluidas_view")
    
    @staticmethod
    def fetch_by_mesa(id_mesa):
        return fetch_from_view("reservas_view", {"id_mesa": id_mesa})
    
    @staticmethod
    def fetch_by_garcom(id_garcom):
        return fetch_from_view("reservas_view", {"id_garcom": id_garcom})

    @staticmethod
    def fetch_by_data(data_hora_inicio, data_hora_fim):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_reservas_by_data(%s, %s, %s)", [data_hora_inicio, data_hora_fim, None])
            return cursor.fetchone()[0]