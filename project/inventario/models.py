from django.db import models
from autenticacao.models import Utilizadores

class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=255)
    vende_ingredientes = models.BooleanField(default=False)
    vende_utensilios = models.BooleanField(default=False)
    morada = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedores_view'

    def __str__(self):
        return self.nome


class Carrinhos(models.Model):
    id_carrinho = models.AutoField(primary_key=True, unique=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrinhos_view'

    def __str__(self):
        return f"Carrinho - {self.data_compra}"
    

class Ingredientes(models.Model):
    id_ingrediente = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    unidade_medida = models.CharField(max_length=50)
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, db_column='id_fornecedor')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientes_view'

    def __str__(self):
        return self.nome


class IngredientesCarrinhos(models.Model):
    id_ingrediente_carrinho = models.AutoField(primary_key=True, unique=True)
    id_ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, db_column='id_ingrediente')
    id_administrador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_administrador')
    id_carrinho = models.ForeignKey(Carrinhos, on_delete=models.CASCADE, db_column='id_carrinho')
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientescarrinhos_view'

    def __str__(self):
        return f"{self.id_ingrediente.nome} - {self.quantidade}"


class Utensilios(models.Model):
    id_utensilio = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, db_column='id_fornecedor')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'utensilios_view'

    def __str__(self):
        return self.nome


class UtensiliosCarrinhos(models.Model):
    id_utensilio_carrinho = models.AutoField(primary_key=True, unique=True)
    id_utensilio = models.ForeignKey(Utensilios, on_delete=models.CASCADE, db_column='id_utensilio')
    id_administrador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_administrador')
    id_carrinho = models.ForeignKey(Carrinhos, on_delete=models.CASCADE, db_column='id_carrinho')
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'utensilioscarrinhos_view'

    def __str__(self):
        return f"{self.id_utensilio.nome} - {self.quantidade}"
    

class Instrucoes(models.Model):
    id_instrucao = models.AutoField(primary_key=True, unique=True)
    numero_sequencia = models.IntegerField()
    id_receita = models.ForeignKey('Receitas', on_delete=models.CASCADE, db_column='id_receita', related_name='instrucoes')
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrucoes_view'

    def __str__(self):
        return f"{self.id_receita} - Passo {self.numero_sequencia}"
    

class Receitas(models.Model):
    id_receita = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=100)
    duracao = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    ingredientes = models.ManyToManyField(Ingredientes, through='IngredientesReceitas')
    utensilios = models.ManyToManyField(Utensilios, through='UtensiliosReceitas')

    class Meta:
        managed = False
        db_table = 'receitas_view'

    def __str__(self):
        return self.nome


class UtensiliosReceitas(models.Model):
    id_utensilio_receita = models.AutoField(primary_key=True, unique=True)
    id_utensilio = models.ForeignKey(Utensilios, on_delete=models.CASCADE, db_column='id_utensilio')
    id_receita = models.ForeignKey(Receitas, on_delete=models.CASCADE, db_column='id_receita')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'utensiliosreceitas_view'

    def __str__(self):
        return f"{self.id_utensilio.nome} - {self.id_receita.nome}"
    

class IngredientesReceitas(models.Model):
    id_ingrediente_receita = models.AutoField(primary_key=True, unique=True)
    id_ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, db_column='id_ingrediente')
    id_receita = models.ForeignKey(Receitas, on_delete=models.CASCADE, db_column='id_receita')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientesreceitas_view'

    def __str__(self):
        return f"{self.id_ingrediente.nome} - {self.id_receita.nome}"

