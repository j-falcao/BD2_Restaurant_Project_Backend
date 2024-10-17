from django.db import models


class pedido(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=False)
    id_utilizador = models.IntegerField()
    id_mesa = models.IntegerField()
    id_garcom = models.IntegerField()
    db_table = 'pedidos'

    def __str__(self):
        return self.nome
    
class pedido_produto(models.Model):
    id_pedido = models.IntegerField()
    id_produto = models.IntegerField()
    id_utilizador = models.IntegerField()
    db_table = 'pedidos_produtos'

    def __str__(self):
        return self.nome