from django.db import models
class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    numero = models.IntegerField()

    class Meta:
        db_table = 'mesas'

    def __str__(self):
        return f"Mesa {self.id_mesa}"

class Pedido(models.Model):
    garcom = models.ForeignKey('auth.Garcom', on_delete=models.CASCADE)
    cliente = models.ForeignKey('auth.Utilizador', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=False)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'pedidos'

    def __str__(self):
        return f"Pedido {self.id} - {self.data_hora}"

class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_produto = models.IntegerField()
    id_utilizador = models.IntegerField()
    
    class Meta:
        db_table = 'pedidos_produtos'

    def __str__(self):
        return f"Produto {self.id_produto} no Pedido {self.pedido.id}"
