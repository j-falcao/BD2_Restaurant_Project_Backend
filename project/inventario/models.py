from django.db import models
from autenticacao.models import Utilizador

class Carrinho(models.Model):
    id_carrinho = models.AutoField(primary_key=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'carrinho'

    def __str__(self):
        return f"Carrinho - {self.data_compra}"


class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    ingredientes = models.BooleanField(default=False)
    utensilios = models.BooleanField(default=False)
    morada = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'fornecedor'

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    unidade_medida = models.CharField(max_length=50)
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, db_column='id_fornecedor')

    class Meta:
        managed = False
        db_table = 'ingrediente'

    def __str__(self):
        return self.nome


class IngredienteCarrinho(models.Model):
    id_ingrediente_administrador = models.AutoField(primary_key=True)
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, db_column='id_ingrediente')
    id_administrador = models.ForeignKey(Utilizador, on_delete=models.CASCADE, db_column='id_administrador')
    id_carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, db_column='id_carrinho')
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ingredientecarrinho'

    def __str__(self):
        return f"{self.id_ingrediente.nome} - {self.quantidade}"


class Utensilio(models.Model):
    id_utensilio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, db_column='id_fornecedor')

    class Meta:
        managed = False
        db_table = 'utensilio'

    def __str__(self):
        return self.nome


class UtensilioCarrinho(models.Model):
    id_utensilio_carrinho = models.AutoField(primary_key=True)
    id_utensilio = models.ForeignKey(Utensilio, on_delete=models.CASCADE, db_column='id_utensilio')
    id_administrador = models.ForeignKey(Utilizador, on_delete=models.CASCADE, db_column='id_administrador')
    id_carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, db_column='id_carrinho')
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'utensiliocarrinho'

    def __str__(self):
        return f"{self.id_utensilio.nome} - {self.quantidade}"


class Receita(models.Model):
    id_receita = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    estimativa_tempo = models.TimeField()

    class Meta:
        managed = False
        db_table = 'receita'

    def __str__(self):
        return self.nome


class UtensilioReceita(models.Model):
    id_utensilio_receita = models.AutoField(primary_key=True)
    id_utensilio = models.ForeignKey(Utensilio, on_delete=models.CASCADE, db_column='id_utensilio')
    id_receita = models.ForeignKey(Receita, on_delete=models.CASCADE, db_column='id_receita')

    class Meta:
        managed = False
        db_table = 'utensilioreceita'

    def __str__(self):
        return f"{self.id_utensilio.nome} - {self.id_receita.nome}"


class Instrucao(models.Model):
    id_instrucao = models.AutoField(primary_key=True)
    id_receita = models.ForeignKey(Receita, on_delete=models.CASCADE, db_column='id_receita')
    numero_sequencia = models.IntegerField()
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'instrucao'

    def __str__(self):
        return f"{self.id_receita.nome} - Passo {self.numero_sequencia}"
