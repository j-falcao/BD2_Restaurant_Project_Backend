from django.db import models

class Pedido(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=False)
    id_utilizador = models.IntegerField()
    id_mesa = models.IntegerField()
    id_garcom = models.ForeignKey('garcom.Garcom', on_delete=models.CASCADE, related_name='pedidos')
    
    class Meta:
        db_table = 'pedidos'

    def __str__(self):
        return f"Pedido {self.id} - {self.data_hora}"

class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='produtos')
    id_produto = models.IntegerField()
    id_utilizador = models.IntegerField()
    
    class Meta:
        db_table = 'pedidos_produtos'

    def __str__(self):
        return f"Produto {self.id_produto} no Pedido {self.pedido.id}"
