from django.db import models
class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    estado = models.ForeignKey('EstadoMesa', on_delete=models.CASCADE)
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mesas'

    def __str__(self):
        return f"Mesa {self.id_mesa}"
    
class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data_hora_inicio = models.DateTimeField(auto_now_add=True)
    data_hora_fim = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'reservas'

    def __str__(self):
        return f"Reserva {self.id_reserva}"


class EstadoMesa(models.Model):
    id_estadoMesa = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estados_mesas'

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    garcom = models.ForeignKey('cargos.Garcom', on_delete=models.CASCADE)
    cliente = models.ForeignKey('cargos.Cliente', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=False)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    
    class Meta:
        managed = False
        db_table = 'pedidos'

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.data_hora}"

class PedidoProduto(models.Model):
    id_pedidoProduto = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    
    class Meta:
        managed = False
        db_table = 'pedidos_produtos'

    def __str__(self):
        return f"Produto {self.produto} no Pedido {self.pedido}"


class PedidoProduto_OpcaoItem(models.Model):
    id_pedidoProduto_opcaoItem = models.AutoField(primary_key=True)
    opcaoItem = models.ForeignKey('produtos.OpcaoItem', on_delete=models.CASCADE)
    PedidoProduto = models.ForeignKey(PedidoProduto, on_delete=models.CASCADE)
    
    class Meta:
        managed = False
        db_table = 'pedidos_produtos_opcoes'

    def __str__(self):
        return f"Opcao {self.opcaoItem} no Pedido {self.PedidoProduto}"