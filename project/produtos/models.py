from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    is_item = models.BooleanField()
    is_menu = models.BooleanField()
    nome = models.CharField(max_length=100)
    url_imagem = models.URLField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'produto'

    def __str__(self):
        return self.nome


class Item(models.Model):
    id_item = models.OneToOneField(Produto, on_delete=models.CASCADE, primary_key=True, related_name='item', db_column='id_item')

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return self.id_produto.nome


class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item, related_name='tipos', through='ItemTipo')

    class Meta:
        managed = False
        db_table = 'tipo'

    def __str__(self):
        return self.nome


class ItemTipo(models.Model):
    id_item_tipo = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE, db_column='id_item')
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'itemtipo'

    def __str__(self):
        return f"Item: {self.id_item} - Tipo: {self.id_tipo}"


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item, related_name='categorias', through='ItemCategoria')

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.nome


class ItemCategoria(models.Model):
    id_item_categoria = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE, db_column='id_item')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'itemcategoria'

    def __str__(self):
        return f'{self.id_item} - {self.id_categoria}'


class Opcao(models.Model):
    id_opcao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    itens = models.ManyToManyField(Item, related_name='opcoes', through='OpcaoItem')

    class Meta:
        managed = False
        db_table = 'opcao'

    def __str__(self):
        return self.nome


class OpcaoItem(models.Model):
    id_opcao_item = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    id_opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'itemopcao'

    def __str__(self):
        return f"{self.id_item} - {self.id_opcao}"


class Menu(models.Model):
    id_menu = models.OneToOneField(Produto, on_delete=models.CASCADE, primary_key=True, related_name='produto_menu', db_column='id_menu')
    itens = models.ManyToManyField(Item, related_name='menus', through='MenuItem')

    class Meta:
        managed = False
        db_table = 'menu'

    def __str__(self):
        return self.id_produto.nome


class MenuItem(models.Model):
    id_menu_item = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, db_column='id_menu')
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE, db_column='id_item')

    class Meta:
        managed = False
        db_table = 'menuitem'

    def __str__(self):
        return f'Menu: {self.id_menu} - Item: {self.id_item}'


class DiaSemana(models.Model):
    id_dia_semana = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    menus = models.ManyToManyField(Menu, related_name='dias', through='MenuDiaSemana')

    class Meta:
        managed = False
        db_table = 'diasemana'

    def __str__(self):
        return self.nome


class MenuDiaSemana(models.Model):
    id_menu_dia_semana = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, db_column='id_menu')
    id_dia_semana = models.ForeignKey(DiaSemana, on_delete=models.CASCADE, db_column='id_dia_semana')
    almoco = models.BooleanField()
    jantar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'menudiasemana'

    def __str__(self):
        return f'Menu: {self.id_menu} - Dia: {self.id_dia_semana} - Almoço: {self.almoco} - Jantar: {self.jantar}'
