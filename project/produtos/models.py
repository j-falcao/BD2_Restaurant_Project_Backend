from django.db import models
from project.utils.db_utils import fetch_from_view


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
        db_table = 'produtos'

    def __str__(self):
        return f"Produto: {self.id_produto} - {self.nome}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('produtos')

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

    def __str__(self):
        return f"Categoria: {self.id_categoria} - {self.designacao}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('categorias')


class Tipos(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos'

    def __str__(self):
        return f"Tipo: {self.id_tipo} - {self.designacao}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('tipos')

class Opcoes(models.Model):
    id_opcao = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'opcoes'

    def __str__(self):
        return f"Opcao: {self.id_opcao} - {self.designacao}"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('opcoes')
    

class Itens(models.Model):
    id_item = models.OneToOneField(Produtos, on_delete=models.CASCADE, primary_key=True, related_name='produto_item', db_column='id_item')
    categorias = models.ManyToManyField(Categorias, related_name='itens', through='itenscategorias')
    tipos = models.ManyToManyField(Tipos, related_name='itens', through='itenstipos')
    opcoes = models.ManyToManyField(Opcoes, related_name='itens', through='itensopcoes')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens'

    def __str__(self):
        return f"Item: {self.id_item}"
    
    @staticmethod
    def fetch_by_id(id_item):
        return fetch_from_view('itens', {'id_item': id_item})

    @staticmethod
    def fetch_all():
        return fetch_from_view('itens')

    @staticmethod
    def fetch_by_menu():
        return fetch_from_view('itens', )


class ItensCategorias(models.Model):
    id_item_categoria = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, db_column='id_categoria')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itenscategorias'

    def __str__(self):
        return f'ItemCategoria: <Item: {self.id_item} - Categoria: {self.id_categoria}>'
    
    @staticmethod
    def fetch_by_item(id_item):
        return fetch_from_view('itenscategorias', {'id_item': id_item})

    @staticmethod
    def fetch_by_categoria(id_categoria):
        return fetch_from_view('itenscategorias', {'id_categoria': id_categoria})


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
        db_table = 'itenstipos'

    def __str__(self):
        return f"ItemTipo: <Item: {self.id_item} - Tipo: {self.id_tipo}>"
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('itenstipos')
    
    @staticmethod
    def fetch_by_id(id_item_tipo):
        return fetch_from_view('itenstipos', {'id_item_tipo': id_item_tipo})
    
    @staticmethod
    def fetch_by_item(id_item):
        return fetch_from_view('itenstipos', {'id_item': id_item})


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
        db_table = 'itensopcoes'

    def __str__(self):
        return f"ItemOpcao <Item: {self.id_item} - Opcao: {self.id_opcao}>"

    @staticmethod
    def fetch_all():
        return fetch_from_view('itensopcoes')
    
    @staticmethod
    def fetch_by_id(id_item_opcao):
        return fetch_from_view('itensopcoes', {'id_item_opcao': id_item_opcao})
    
    @staticmethod
    def fetch_by_item(id_item):
        return fetch_from_view('itensopcoes', {'id_item': id_item})


class Menus(models.Model):
    id_menu = models.OneToOneField(Produtos, on_delete=models.CASCADE, primary_key=True, related_name='produto_menu', db_column='id_menu')
    itens = models.ManyToManyField(Itens, related_name='menus', through='ItensMenus')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus'

    def __str__(self):
        return f"Menu: {self.id_menu.id_produto} - {self.id_menu.nome}"
    
    @staticmethod
    def fetch_by_id(id_menu):
        return fetch_from_view('menus', {'id_menu': id_menu})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('menus')


class ItensMenus(models.Model):
    id_item_menu = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_menu = models.ForeignKey(Menus, on_delete=models.CASCADE, db_column='id_menu')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itensmenus'

    def __str__(self):
        return f'ItemMenu: <Menu: {self.id_menu} - Item: {self.id_item}>'
    
    @staticmethod
    def fetch_by_id(id_item_menu):
        return fetch_from_view('itensmenus', {'id_item_menu': id_item_menu})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('itensmenus')
    
    @staticmethod
    def fetch_by_menu(id_menu):
        return fetch_from_view('itensmenus', {'id_menu': id_menu})
    
    @staticmethod
    def fetch_by_item(id_item):
        return fetch_from_view('itensmenus', {'id_item': id_item})


class DiasSemana(models.Model):
    id_dia_semana = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    menus = models.ManyToManyField(Menus, related_name='dias', through='MenusDiasSemana')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'diassemana'

    def __str__(self):
        return f"Dia: {self.id_dia_semana} - {self.nome}"
    
    @staticmethod
    def fetch_by_id(id_dia_semana):
        return fetch_from_view('diassemana', {'id_dia_semana': id_dia_semana})
    
    @staticmethod
    def fetch_all():
        return fetch_from_view('diassemana')


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
        db_table = 'menusdiassemana'

    def __str__(self):
        return f'MenuDiaSemana: <Menu: {self.id_menu} - Dia: {self.id_dia_semana} - Almoço: {self.almoco} - Jantar: {self.jantar}>'
    
    @staticmethod
    def fetch_by_menu(id_menu):
        return fetch_from_view('menusdiassemana', {'id_menu': id_menu})
    
    @staticmethod
    def fetch_by_dia_semana(id_dia_semana):
        return fetch_from_view('menusdiassemana', {'id_dia_semana': id_dia_semana})
