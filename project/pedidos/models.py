from django.db import models
from autenticacao.models import Utilizadores


class EstadosMesas(models.Model):
    id_estado_mesa = models.AutoField(primary_key=True, unique=True)
    designacao = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadosmesas_view'

    def __str__(self):
        return self.designacao


class Mesas(models.Model):
    id_mesa = models.AutoField(primary_key=True, unique=True)
    id_estado_mesa = models.ForeignKey(
        EstadosMesas, on_delete=models.CASCADE, db_column='id_estado_mesa')
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


class Servicos(models.Model):
    id_servico = models.AutoField(primary_key=True, unique=True)
    id_mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE, null=True,
                                blank=True, related_name="servicos", db_column='id_mesa')
    id_garcom = models.ForeignKey(Utilizadores, on_delete=models.CASCADE,
                                  null=True, blank=True, related_name="servicos", db_column='id_garcom')
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


class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True, unique=True)
    id_mesa = models.ForeignKey(
        Mesas, on_delete=models.CASCADE, db_column='id_mesa')
    data_hora = models.DateTimeField(auto_now_add=True)
    minutos_antes = models.DurationField()
    minutos_depois = models.DurationField()
    id_servico = models.ForeignKey(Servicos, on_delete=models.CASCADE,
                                   null=True, blank=True, related_name="reserva", db_column='id_servico')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservas_view'

    def __str__(self):
        return f"Reserva {self.id_reserva} na Mesa {self.id_mesa}"


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True, unique=True)
    id_servico = models.ForeignKey(Servicos, on_delete=models.CASCADE,
                                   null=True, blank=True, related_name="pedidos", db_column='id_servico')
    produtos = models.ManyToManyField(
        'produtos.Produtos', through='PedidosProdutos', related_name='pedidos')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def data_hora_valida(self):
        if self.created_at < self.id_servico.data_hora_inicio:
            return False
        elif self.id_servico.data_hora_fim is not None and self.created_at > self.id_servico.data_hora_fim:
            return False
        return True

    class Meta:
        managed = False
        db_table = 'pedidos_view'

    def __str__(self):
        return f"Serviço {self.id_servico} - Pedido {self.id_pedido} - {self.data_hora}"


class PedidosProdutos(models.Model):
    id_pedido_produto = models.AutoField(primary_key=True, unique=True)
    id_pedido = models.ForeignKey(
        Pedidos, on_delete=models.CASCADE, db_column='id_pedido')
    id_produto = models.ForeignKey(
        'produtos.Produtos', on_delete=models.CASCADE, db_column='id_produto')
    id_cozinheiro = models.ForeignKey(
        Utilizadores, on_delete=models.CASCADE, db_column='id_cozinheiro')
    opcoes = models.ManyToManyField(
        'produtos.ItensOpcoes', through='PedidosProdutosItensOpcoes', related_name='pedido_produto')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidosprodutos'

    def __str__(self):
        return f"Produto {self.id_produto} no Pedido {self.id_pedido}"


class PedidosProdutosItensOpcoes(models.Model):
    id_pedido_produto_item_opcao = models.AutoField(primary_key=True, unique=True)
    id_item_opcao = models.ForeignKey(
        'produtos.ItensOpcoes', on_delete=models.CASCADE, db_column='id_item_opcao')
    id_pedido_produto = models.ForeignKey(
        PedidosProdutos, on_delete=models.CASCADE, db_column='id_pedido_produto')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidosprodutositensopcoes'

    def __str__(self):
        return f"Opção {self.id_item_opcao} no Produto do Pedido {self.id_pedido_produto}"
    

