from django.db import models

class Mesa(models.Model):
    """
    Representa uma mesa no restaurante, com um número e um estado associado.
    """
    id_mesa = models.AutoField(primary_key=True)
    estado = models.ForeignKey('EstadoMesa', on_delete=models.CASCADE)
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mesa'

    def __str__(self):
        return f"Mesa {self.numero}"


class Reserva(models.Model):
    """
    Representa uma reserva para uma mesa, com data e hora de início e fim.
    """
    id_reserva = models.AutoField(primary_key=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data_hora_inicio = models.DateTimeField(auto_now_add=True)
    data_hora_fim = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'reserva'

    def __str__(self):
        return f"Reserva {self.id_reserva} na Mesa {self.mesa}"


class EstadoMesa(models.Model):
    """
    Define o estado atual de uma mesa, como 'Disponível', 'Ocupada', etc.
    """
    id_estado_mesa = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estadomesa'

    def __str__(self):
        return self.estado


class Pedido(models.Model):
    """
    Representa um pedido feito por um cliente, incluindo a mesa, o garçom e se foi feito online.
    """
    id_pedido = models.AutoField(primary_key=True)
    garcom = models.ForeignKey('cargos.Garcom', on_delete=models.CASCADE)
    cliente = models.ForeignKey('cargos.Cliente', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=False)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    produtos = models.ManyToManyField('produtos.Produto', through='PedidoProduto', related_name='pedidos')

    class Meta:
        managed = False
        db_table = 'pedido'

    def __str__(self):
        return f"Pedido {self.id_pedido} - Mesa {self.mesa.numero} - {self.data_hora}"


class PedidoProduto(models.Model):
    """
    Intermediário para produtos em um pedido específico, permitindo associar múltiplos produtos a um pedido.
    """
    id_pedido_produto = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    opcoes = models.ManyToManyField('produtos.OpcaoItem', through='PedidoProdutoOpcaoItem', related_name='pedido_produtos')

    class Meta:
        managed = False

    def __str__(self):
        return f"Produto {self.produto} no Pedido {self.pedido}"


class PedidoProdutoOpcaoItem(models.Model):
    """
    Intermediário para as opções associadas a um produto específico dentro de um pedido.
    """
    id_pedido_produto_opcao_item = models.AutoField(primary_key=True)
    opcao_item = models.ForeignKey('produtos.OpcaoItem', on_delete=models.CASCADE)
    pedido_produto = models.ForeignKey(PedidoProduto, on_delete=models.CASCADE)

    class Meta:
        managed = False

    def __str__(self):
        return f"Opção {self.opcao_item} no Produto do Pedido {self.pedido_produto}"
