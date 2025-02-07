from django.db import connection, models
from autenticacao.models import Utilizadores
from project.utils.db_utils import fetch_from_view


class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    vende_ingredientes = models.BooleanField(default=False)
    vende_utensilios = models.BooleanField(default=False)
    morada = models.CharField(max_length=255)
    email = models.EmailField()
    telemovel = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedores'

    def __str__(self):
        return f"Fornecedor - {self.nome}"
    
    @staticmethod
    def fetch_by_id(id_fornecedor):
        return fetch_from_view("fornecedores_view", {"id_fornecedor": id_fornecedor})  

    @staticmethod
    def fetch_all():
        return fetch_from_view("fornecedores_view")


class Ingredientes(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    unidade_medida = models.CharField(max_length=50)
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_fornecedor = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientes'

    def __str__(self):
        return f"Ingrediente - {self.nome}"
    
    @staticmethod
    def fetch_by_id(id_ingrediente):
        return fetch_from_view("ingredientes_view", {"id_ingrediente": id_ingrediente})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("ingredientes_view")
    
    @staticmethod
    def fetch_by_fornecedor(id_fornecedor):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_ingredientes_by_fornecedor(%s, %s)', [id_fornecedor, None])
            return cursor.fetchone()[0]


class Utensilios(models.Model):
    id_utensilio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url_imagem = models.URLField(blank=True, null=True)
    quantidade_stock = models.IntegerField()
    unidade_medida = models.CharField(max_length=50)
    limite_stock = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_fornecedor = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'utensilios'

    def __str__(self):
        return f"Utensilio - {self.nome}"

    @staticmethod
    def fetch_by_id(id_utensilio):
        return fetch_from_view("utensilios_view", {"id_utensilio": id_utensilio})

    @staticmethod
    def fetch_all():
        return fetch_from_view("utensilios_view")
    
    @staticmethod
    def fetch_by_fornecedor(id_fornecedor):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_utensilios_by_fornecedor(%s, %s)', [id_fornecedor, None])
            return cursor.fetchone()[0]

class TiposCarrinhos(models.Model):
    id_tipo_carrinho = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposcarrinhos'

    def __str__(self):
        return f"Tipo de carrinho - {self.designacao}"

    @staticmethod
    def fetch_by_id(id_tipo_carrinho):
        return fetch_from_view("tiposcarrinhos_view", {"id_tipo_carrinho": id_tipo_carrinho})

    @staticmethod
    def fetch_all():
        return fetch_from_view("tiposcarrinhos_view")


class Carrinhos(models.Model):
    id_carrinho = models.AutoField(primary_key=True)
    id_tipo_carrinho = models.ForeignKey(
        TiposCarrinhos, on_delete=models.CASCADE, db_column='id_tipo_carrinho')
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_artigos = models.IntegerField()
    data_compra = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Carrinho {self.id_carrinho}, com {self.qtd_artigos} artigos, preco total {self.preco_total}, comprado em {self.data_compra}"

    class Meta:
        managed = False
        db_table = 'carrinhos'

    @staticmethod
    def fetch_atual_ingredientes():
        return fetch_from_view("carrinho_atual_ingredientes_view")

    @staticmethod
    def fetch_atual_utensilios():
        return fetch_from_view("carrinho_atual_utensilios_view")

    @staticmethod
    def fetch_by_id(id_carrinho):
        return fetch_from_view("carrinhos_view", {"id_carrinho": id_carrinho})

    @staticmethod
    def fetch_all():
        return fetch_from_view("carrinhos_view")


class IngredientesCarrinhos(models.Model):
    id_ingrediente_carrinho = models.AutoField(primary_key=True)
    id_ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, db_column='id_ingrediente')
    id_administrador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_administrador')
    id_carrinho = models.ForeignKey(Carrinhos, on_delete=models.CASCADE, db_column='id_carrinho')
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"IngredienteCarrinho - Ingrediente: {self.id_ingrediente} - Carrinho: {self.id_carrinho} - Quantidade: {self.quantidade}"

    class Meta:
        managed = False
        db_table = 'ingredientescarrinhos'

    @staticmethod
    def fetch_by_carrinho_atual():
        return fetch_from_view("ingredientescarrinho_atual_view")
    
    @staticmethod
    def fetch_by_carrinho(id_carrinho):
        return fetch_from_view("ingredientescarrinho_view", {"id_carrinho": id_carrinho})
    

class UtensiliosCarrinhos(models.Model):
    id_utensilio_carrinho = models.AutoField(primary_key=True)
    id_utensilio = models.ForeignKey(Utensilios, on_delete=models.CASCADE, db_column='id_utensilio')
    id_administrador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE, db_column='id_administrador')
    id_carrinho = models.ForeignKey(Carrinhos, on_delete=models.CASCADE, db_column='id_carrinho')
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'utensilios_carrinhos'

    def __str__(self):
        return f"UtensilioCarrinho - Utensilio: {self.id_utensilio} - Carrinho: {self.id_carrinho} - Quantidade: {self.quantidade}"
    
    @staticmethod
    def fetch_by_carrinho_atual():
        return fetch_from_view("utensilioscarrinho_atual_view")
    
    @staticmethod
    def fetch_by_carrinho(id_carrinho):
        return fetch_from_view("utensilioscarrinho_view", {"id_carrinho": id_carrinho})
    


class Instrucoes(models.Model):
    id_instrucao = models.AutoField(primary_key=True)
    id_receita = models.ForeignKey('Receitas', on_delete=models.CASCADE, db_column='id_receita')
    numero_sequencia = models.IntegerField()
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrucoes'

    def __str__(self):
        return f"Instrução: {self.id_instrucao} - Receita {self.id_receita} - Passo {self.numero_sequencia}"
    
    @staticmethod
    def fetch_by_receita(id_receita, numero_sequencia=None):
        filters = {"id_receita": id_receita}
        if numero_sequencia:
            filters["numero_sequencia"] = numero_sequencia

        return fetch_from_view("instrucoes_view", filters)


class Receitas(models.Model):
    id_receita = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    duracao = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    ingredientes = models.ManyToManyField(Ingredientes, through='IngredientesReceitas')
    utensilios = models.ManyToManyField(Utensilios, through='UtensiliosReceitas')

    class Meta:
        managed = False
        db_table = 'receitas'

    def __str__(self):
        return f"Receita - {self.nome}"

    @staticmethod
    def fetch_by_id(id_receita):
        return fetch_from_view("receitas_view", {"id_receita": id_receita})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("receitas_view")


class IngredientesReceitas(models.Model):
    id_ingrediente_receita = models.AutoField(primary_key=True)
    id_ingrediente = models.ForeignKey(
        Ingredientes, on_delete=models.CASCADE, db_column='id_ingrediente')
    id_receita = models.ForeignKey(
        Receitas, on_delete=models.CASCADE, db_column='id_receita')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientesreceitas'

    def __str__(self):
        return f"IngredienteReceita - Ingrediente: {self.id_ingrediente} - Receita: {self.id_receita}"
    
    @staticmethod
    def fetch_by_ingrediente(id_ingrediente):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_receitas_by_ingrediente(%s, %s)', [id_ingrediente, None])
            return cursor.fetchone()[0]
   
    @staticmethod
    def fetch_by_receita(id_receita):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_ingredientes_by_receita(%s, %s)', [id_receita, None])
            return cursor.fetchone()[0]
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("ingredientesreceitas_view")


class UtensiliosReceitas(models.Model):
    id_utensilio_receita = models.AutoField(primary_key=True)
    id_utensilio = models.ForeignKey(
        Utensilios, on_delete=models.CASCADE, db_column='id_utensilio')
    id_receita = models.ForeignKey(
        Receitas, on_delete=models.CASCADE, db_column='id_receita')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'utensiliosreceitas'

    def __str__(self):
        return f"UtensilioReceita - Utensilio: {self.id_utensilio} - Receita: {self.id_receita}"
    
    @staticmethod
    def fetch_by_utensilio(id_utensilio):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_receitas_by_utensilio(%s, %s)', [id_utensilio, None])
            return cursor.fetchone()[0]
   
    @staticmethod
    def fetch_by_receita(id_receita):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_utensilios_by_receita(%s, %s)', [id_receita, None])
            return cursor.fetchone()[0]
    
    @staticmethod
    def fetch_all():
        return fetch_from_view("utensiliosreceitas_view")