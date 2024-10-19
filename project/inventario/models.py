from django.db import models
from auth.models import Administrador

class Carrinho(models.Model):
    id_carrinho = models.AutoField(primary_key=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateTimeField()

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
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class IngredienteValidade(models.Model):
    id_ingredienteValidade = models.AutoField(primary_key=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    data_validade = models.DateField()

    def __str__(self):
        return f"{self.ingrediente.nome} - {self.data_validade}"
    
    
class IngredienteAdministrador(models.Model):
    id_ingredienteAdministrador = models.AutoField(primary_key=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.ingrediente.nome} - {self.quantidade}"


class Utensilio(models.Model):
    id_utensilio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class UtensilioAdministrador(models.Model):
    id_utensilioAdministrador = models.AutoField(primary_key=True)
    utensilio = models.ForeignKey(Utensilio, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.utensilio.nome} - {self.quantidade}"


class Receita(models.Model):
    id_receita = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    estimativaTempo = models.TimeField()

    def __str__(self):
        return self.nome


class UtensilioReceita(models.Model):
    id_utensilioReceita = models.AutoField(primary_key=True)
    utensilio = models.ForeignKey(Utensilio, on_delete=models.CASCADE)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.utensilio.nome} - {self.receita.nome}"



class Instucao(models.Model):
    id_instucao = models.AutoField(primary_key=True)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    numeroSequencia = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.receitaNome} - Passo {self.numeroSequencia}"