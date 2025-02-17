from django.db import connection, models
from project.utils.db_utils import fetch_from_view
from inventario.models import *


class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    item = models.BooleanField()
    menu = models.BooleanField()
    nome = models.CharField(max_length=100)
    url_imagem = models.URLField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos_view'

    def __str__(self):
        return f"Produto: {self.id_produto} - {self.nome}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('produtos_view')
    

class Instrucoes(models.Model):
    id_instrucao = models.AutoField(primary_key=True)
    id_receita = models.ForeignKey('Receitas', on_delete=models.CASCADE, db_column='id_receita')
    numero_sequencia = models.IntegerField()
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrucoes_view'

    def __str__(self):
        return f"Instrução: {self.id_instrucao} - Receita {self.id_receita} - Passo {self.numero_sequencia}"
    
    @staticmethod
    def fetch_by_receita(id_receita):
        return fetch_from_view("instrucoes_view", {"id_receita": id_receita})


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
        db_table = 'receitas_view'

    def __str__(self):
        return f"Receita - {self.nome}"

    @staticmethod
    def fetch_by_id(id_receita):
        return fetch_from_view("receitas_view", {"id_receita": id_receita})
        
    @staticmethod
    def fetch_all():
        return fetch_from_view("receitas_view")
    
    @staticmethod
    def fetch_by_ingrediente(id_ingrediente):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_receitas_by_ingrediente(%s, %s)', [id_ingrediente, None])
            return cursor.fetchone()[0]

    @staticmethod
    def fetch_by_utensilio(id_utensilio):
        with connection.cursor() as cursor:
            cursor.execute('CALL get_receitas_by_utensilio(%s, %s)', [id_utensilio, None])
            return cursor.fetchone()[0]


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
        db_table = 'ingredientesreceitas_view'

    def __str__(self):
        return f"IngredienteReceita - Ingrediente: {self.id_ingrediente} - Receita: {self.id_receita}"


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
        db_table = 'utensiliosreceitas_view'

    def __str__(self):
        return f"UtensilioReceita - Utensilio: {self.id_utensilio} - Receita: {self.id_receita}"
    

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias_view'

    def __str__(self):
        return f"Categoria: {self.id_categoria} - {self.designacao}"
    
    @staticmethod
    def fetch_by_id(id_categoria):
        return fetch_from_view('categorias_view', {'id_categoria': id_categoria})

    @staticmethod
    def fetch_all():
        return fetch_from_view('categorias_view')

    @staticmethod
    def fetch_by_item(id_item):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_categorias_by_item(%s, %s)", [id_item, None])
            return cursor.fetchone()[0]


class Tipos(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_view'

    def __str__(self):
        return f"Tipo: {self.id_tipo} - {self.designacao}"
    
    @staticmethod
    def fetch_by_id(id_tipo):
        return fetch_from_view('tipos_view', {'id_tipo': id_tipo})

    @staticmethod
    def fetch_all():
        return fetch_from_view('tipos_view')
    
    @staticmethod
    def fetch_by_item(id_item):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_tipos_by_item(%s, %s)", [id_item, None])            
            return cursor.fetchone()[0]


class Opcoes(models.Model):
    id_opcao = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'opcoes_view'

    def __str__(self):
        return f"Opcao: {self.id_opcao} - {self.designacao}"
    
    @staticmethod
    def fetch_by_id(id_opcao):
        return fetch_from_view('opcoes_view', {'id_opcao': id_opcao})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('opcoes_view')
    
    @staticmethod
    def fetch_by_item(id_item):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_opcoes_by_item(%s, %s)", [id_item, None])            
            return cursor.fetchone()[0]

    
class Itens(models.Model):
    id_item = models.OneToOneField(Produtos, on_delete=models.CASCADE, primary_key=True, related_name='produto_item', db_column='id_item')
    categorias = models.ManyToManyField(Categorias, related_name='itens', through='itenscategorias')
    tipos = models.ManyToManyField(Tipos, related_name='itens', through='itenstipos')
    opcoes = models.ManyToManyField(Opcoes, related_name='itens', through='itensopcoes')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens_view'

    def __str__(self):
        return f"Item: {self.id_item}"
    
    @staticmethod
    def fetch_by_id(id_item):
        return fetch_from_view('itens_view', {'id_item': id_item})

    @staticmethod
    def fetch_all():
        return fetch_from_view('itens_view')
    
    @staticmethod
    def fetch_by_categoria(id_categoria):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_itens_by_categoria(%s, %s)", [id_categoria, None])
            return cursor.fetchone()[0]
    
    @staticmethod
    def fetch_by_tipo(id_tipo):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_itens_by_tipo(%s, %s)", [id_tipo, None])
            return cursor.fetchone()[0]
    
    @staticmethod
    def fetch_by_opcao(id_opcao):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_itens_by_opcao(%s, %s)", [id_opcao, None])            
            return cursor.fetchone()[0]
        
    @staticmethod
    def fetch_by_menu(id_menu):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_itens_by_menu(%s, %s)", [id_menu, None])            
            return cursor.fetchone()[0]


class ItensCategorias(models.Model):
    id_item_categoria = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, db_column='id_categoria')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itenscategorias_view'

    def __str__(self):
        return f'ItemCategoria: <Item: {self.id_item} - Categoria: {self.id_categoria}>'


class ItensTipos(models.Model):
    id_item_tipo = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(
        Itens, on_delete=models.CASCADE, db_column='id_item')
    id_tipo = models.ForeignKey(
        Tipos, on_delete=models.CASCADE, db_column='id_tipo')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itenstipos_view'

    def __str__(self):
        return f"ItemTipo: <Item: {self.id_item} - Tipo: {self.id_tipo}>"


class ItensOpcoes(models.Model):
    id_item_opcao = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(
        Itens, on_delete=models.CASCADE, db_column='id_item')
    id_opcao = models.ForeignKey(
        Opcoes, on_delete=models.CASCADE, db_column='id_opcao')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itensopcoes_view'

    def __str__(self):
        return f"ItemOpcao <Item: {self.id_item} - Opcao: {self.id_opcao}>"


class Menus(models.Model):
    id_menu = models.OneToOneField(Produtos, on_delete=models.CASCADE, primary_key=True, related_name='produto_menu', db_column='id_menu')
    itens = models.ManyToManyField(Itens, related_name='menus', through='ItensMenus')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus_view'

    def __str__(self):
        return f"Menu: {self.id_menu.id_produto} - {self.id_menu.nome}"
    
    @staticmethod
    def fetch_by_id(id_menu):
        return fetch_from_view('menus_view', {'id_menu': id_menu})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('menus_view')
    
    @staticmethod
    def fetch_by_item(id_item):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_menus_by_item(%s, %s)", [id_item, None])
            return cursor.fetchone()[0]
        
    @staticmethod
    def fetch_by_diasemana(id_dia_semana):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_menus_by_diasemana(%s, %s)", [id_dia_semana, None])
            return cursor.fetchone()[0]


class ItensMenus(models.Model):
    id_item_menu = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_menu = models.ForeignKey(Menus, on_delete=models.CASCADE, db_column='id_menu')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itensmenus_view'

    def __str__(self):
        return f'ItemMenu: <Menu: {self.id_menu} - Item: {self.id_item}>'


class DiasSemana(models.Model):
    id_dia_semana = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    menus = models.ManyToManyField(Menus, related_name='dias', through='MenusDiasSemana')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'diassemana_view'

    def __str__(self):
        return f"Dia: {self.id_dia_semana} - {self.nome}"
    
    @staticmethod
    def fetch_by_id(id_dia_semana):
        return fetch_from_view('diassemana_view', {'id_dia_semana': id_dia_semana})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('diassemana_view')
    
    @staticmethod
    def fetch_by_menu(id_menu):
        with connection.cursor() as cursor:
            cursor.execute("CALL get_diassemana_by_menu(%s, %s)", [id_menu, None])
            return cursor.fetchone()[0]


class MenusDiasSemana(models.Model):
    id_menu_dia_semana = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey(Menus, on_delete=models.CASCADE, db_column='id_menu')
    id_dia_semana = models.ForeignKey(DiasSemana, on_delete=models.CASCADE, db_column='id_dia_semana')
    almoco = models.BooleanField()
    jantar = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'menusdiassemana_view'

    def __str__(self):
        return f'MenuDiaSemana: <Menu: {self.id_menu} - Dia: {self.id_dia_semana} - Almoço: {self.almoco} - Jantar: {self.jantar}>'