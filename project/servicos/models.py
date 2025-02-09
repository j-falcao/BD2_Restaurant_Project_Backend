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
        db_table = 'estadosmesas'

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
        db_table = 'mesas'

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
        db_table = 'servicos'

    def __str__(self):
        return f"Serviço {self.id_servico} na Mesa {self.id_mesa}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("servicos_view")
    
    @staticmethod
    def fetch_by_id(id_servico):
        return fetch_from_view("servicos_view", {"id_servico": id_servico})
    
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
    def fetch_by_data(data_hora_inicio):
        return fetch_from_view("servicos_view", {"data_hora_inicio": data_hora_inicio}) 


class EstadosReservas(models.Model):
    id_estado_reserva = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadosreservas'

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
        db_table = 'reservas'

    def __str__(self):
        return f"Reserva {self.id_reserva} na Mesa {self.id_mesa}"
    
    
    @staticmethod
    def fetch_by_id(id_reserva):
        return fetch_from_view("reservas_view", {"id_reserva": id_reserva})
    
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
        with connection.cursor() as cursor:
            cursor.execute("CALL get_reservas_by_mesa(%s, %s)", [id_mesa, None])
            return cursor.fetchone()[0]
        
    @staticmethod
    def fetch_by_garcom(id_garcom):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_reservas_by_garcom(%s, %s)", [id_garcom, None])
            return cursor.fetchone()[0]

    @staticmethod
    def fetch_by_data(data_inicio=datetime.now(), data_fim=datetime.now()):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_reservas_by_data(%s, %s, %s)", [data_inicio, data_fim, None])
            return cursor.fetchone()[0]


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_servico = models.ForeignKey(Servicos, on_delete=models.CASCADE, db_column='id_servico')
    produtos = models.ManyToManyField('produtos.Produtos', through='PedidosProdutos', related_name='pedidos')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def data_hora_valida(self):
        if self.created_at < self.id_servico.data_hora_inicio or self.created_at > self.id_servico.data_hora_fim:
            return False
        elif self.id_servico.data_hora_fim is None and self.id_servico.data_hora_fim is not None:
            return False
        return True

    class Meta:
        managed = False
        db_table = 'pedidos'

    def __str__(self):
        return f"Serviço {self.id_servico} - Pedido {self.id_pedido} - {self.created_at}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("pedidos_view")
    
    @staticmethod
    def fetch_by_id(id_pedido):
        return fetch_from_view("pedidos_view", {"id_pedido": id_pedido})
    
    @staticmethod
    def fetch_by_servico(id_servico):
        return fetch_from_view("pedidos_view", {"id_servico": id_servico})


class PedidosProdutos(models.Model):
    id_pedido_produto = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, db_column='id_pedido')
    id_produto = models.ForeignKey('produtos.Produtos', on_delete=models.CASCADE, db_column='id_produto')
    id_cozinheiro = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_cozinheiro')
    # opcoes = models.ManyToManyField('produtos.ItensOpcoes', through='PedidosProdutosItensOpcoes', related_name='pedido_produto')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidosprodutos'

    def __str__(self):
        return f"Produto {self.id_produto} no Pedido {self.id_pedido}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("pedidosprodutos_view")
    
    @staticmethod
    def fetch_by_id(id_pedido_produto):
        return fetch_from_view("pedidosprodutos_view", {"id_pedido_produto": id_pedido_produto})
    
    @staticmethod
    def fetch_by_pedido(id_pedido):
        return fetch_from_view("pedidosprodutos_view", {"id_pedido": id_pedido})