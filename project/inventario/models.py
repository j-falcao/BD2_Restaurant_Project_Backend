from django.db import models
from cargos.models import Utilizador

class Carrinho(models.Model):
    """
    Representa um carrinho de compras, com o preço total e data da compra.
    """
    id_carrinho = models.AutoField(primary_key=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'carrinho'

    def __str__(self):
        return f"Carrinho - {self.data_compra}"


class Fornecedor(models.Model):
    """
    Representa um fornecedor de ingredientes e/ou utensílios para o restaurante.
    """
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
    """
    Representa um ingrediente disponível no estoque, com limite e quantidade atual.
    """
    id_ingrediente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    unidade_medida = models.CharField(max_length=50)
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ingrediente'

    def __str__(self):
        return self.nome


class IngredienteValidade(models.Model):
    """
    Representa a data de validade de um ingrediente específico.
    """
    id_ingrediente_validade = models.AutoField(primary_key=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    data_validade = models.DateField()

    class Meta:
        managed = False

    def __str__(self):
        return f"{self.ingrediente.nome} - {self.data_validade}"


class IngredienteAdministrador(models.Model):
    """
    Tabela intermediária para associar ingredientes com administradores e carrinhos.
    """
    id_ingrediente_administrador = models.AutoField(primary_key=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    class Meta:
        managed = False

    def __str__(self):
        return f"{self.ingrediente.nome} - {self.quantidade}"


class Utensilio(models.Model):
    """
    Representa um utensílio disponível no estoque.
    """
    id_utensilio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'utensilio'

    def __str__(self):
        return self.nome


class UtensilioAdministrador(models.Model):
    """
    Tabela intermediária para associar utensílios com administradores e carrinhos.
    """
    id_utensilio_administrador = models.AutoField(primary_key=True)
    utensilio = models.ForeignKey(Utensilio, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    class Meta:
        managed = False

    def __str__(self):
        return f"{self.utensilio.nome} - {self.quantidade}"


class Receita(models.Model):
    """
    Representa uma receita, com nome e tempo estimado de preparo.
    """
    id_receita = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    estimativa_tempo = models.TimeField()

    class Meta:
        managed = False
        db_table = 'receita'

    def __str__(self):
        return self.nome


class UtensilioReceita(models.Model):
    """
    Tabela intermediária para associar utensílios necessários para uma receita.
    """
    id_utensilio_receita = models.AutoField(primary_key=True)
    utensilio = models.ForeignKey(Utensilio, on_delete=models.CASCADE)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

    class Meta:
        managed = False

    def __str__(self):
        return f"{self.utensilio.nome} - {self.receita.nome}"


class Instrucao(models.Model):
    """
    Representa uma instrução de uma receita específica, com um número sequencial.
    """
    id_instrucao = models.AutoField(primary_key=True)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    numero_sequencia = models.IntegerField()
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'instrucao'

    def __str__(self):
        return f"{self.receita.nome} - Passo {self.numero_sequencia}"
