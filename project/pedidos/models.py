from django.db import models
from autenticacao.models import Utilizador

class EstadoMesa(models.Model):
    id_estado_mesa = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadomesa'

    def __str__(self):
        return self.estado


class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    id_estado_mesa = models.ForeignKey(EstadoMesa, on_delete=models.CASCADE, db_column='id_estado_mesa')
    numero = models.IntegerField()
    capacidade_maxima = models.IntegerField()
    quantidade_ocupantes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa'

    def __str__(self):
        return f"Mesa {self.numero}"


class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True, blank=True, related_name="servicos", db_column='id_mesa')
    id_garcom = models.ForeignKey(Utilizador, on_delete=models.CASCADE, null=True, blank=True, related_name="servicos", db_column='id_garcom')
    data_hora_inicio = models.DateTimeField(auto_now_add=True)
    data_hora_fim = models.DateTimeField(null=True, blank=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'servico'

    def __str__(self):
        return f"Serviço {self.id_servico} na Mesa {self.id_mesa}"


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, db_column='id_mesa')
    data_hora = models.DateTimeField(auto_now_add=True)
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True, related_name="reserva", db_column='id_servico')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'

    def __str__(self):
        return f"Reserva {self.id_reserva} na Mesa {self.id_mesa}"


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True, related_name="pedidos", db_column='id_servico')
    produtos = models.ManyToManyField('produtos.Produto', through='PedidoProduto', related_name='pedidos')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def data_hora_valida(self):
        if self.created_at < self.id_servico.data_hora_inicio:
            return False
        elif self.id_servico.data_hora_fim is not None and self.created_at > self.id_servico.data_hora_fim:
            return False
        return True

    class Meta:
        managed = False
        db_table = 'pedido'

    def __str__(self):
        return f"Serviço {self.id_servico} - Pedido {self.id_pedido} - {self.data_hora}"


class PedidoProduto(models.Model):
    id_pedido_produto = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='id_pedido')
    id_produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE, db_column='id_produto')
    opcoes = models.ManyToManyField('produtos.ItemOpcao', through='PedidoProdutoItemOpcao', related_name='pedido_produtos')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidoproduto'

    def __str__(self):
        return f"Produto {self.id_produto} no Pedido {self.id_pedido}"


class PedidoProdutoItemOpcao(models.Model):
    id_pedido_produto_item_opcao = models.AutoField(primary_key=True)
    id_item_opcao = models.ForeignKey('produtos.ItemOpcao', on_delete=models.CASCADE, db_column='id_item_opcao')
    id_pedido_produto = models.ForeignKey(PedidoProduto, on_delete=models.CASCADE, db_column='id_pedido_produto')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidoprodutoitemopcao'

    def __str__(self):
        return f"Opção {self.id_item_opcao} no Produto do Pedido {self.id_pedido_produto}"
