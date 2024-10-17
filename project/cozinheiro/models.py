from django.db import models

class Cozinheiro(models.Model):
    id_pedido = models.ForeignKey('pedidos.Pedido', on_delete=models.CASCADE)
    id_especialidade = models.ForeignKey('especialidade.Especialidade', on_delete=models.CASCADE)