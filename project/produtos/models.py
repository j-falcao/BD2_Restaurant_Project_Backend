from django.db import models

class Produto(models.Model):
    """
    Representa um produto com informações de disponibilidade no menu e no estoque.
    """
    id_produto = models.AutoField(primary_key=True)
    item = models.BooleanField()
    menu = models.BooleanField()
    nome = models.CharField(max_length=100)
    url_imagem = models.URLField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'produto'

    def __str__(self):
        return self.nome


class Item(models.Model):
    """
    Relaciona-se com o Produto, representando um item específico do menu.
    """
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, primary_key=True, related_name='produto_item')

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return self.produto.nome


class Tipo(models.Model):
    """
    Representa um tipo de item, como 'bebida', 'sobremesa', etc., categorizando o item no menu.
    """
    id_tipo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item, related_name='tipos', through='ItemTipo')

    class Meta:
        managed = False
        db_table = 'tipo'

    def __str__(self):
        return self.nome


class ItemTipo(models.Model):
    """
    Tabela intermediária para a relação entre Item e Tipo.
    """
    id_item_tipo = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        managed = False

    def __str__(self):
        return f"{self.item} - {self.tipo}"


class Categoria(models.Model):
    """
    Representa uma categoria de itens, como 'prato principal', 'entrada', etc.
    """
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item, related_name='categorias', through='ItemCategoria')

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.nome


class ItemCategoria(models.Model):
    """
    Tabela intermediária para a relação entre Item e Categoria.
    """
    id_item_categoria = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        managed = False

    def __str__(self):
        return f'{self.item} - {self.categoria}'


class Opcao(models.Model):
    """
    Representa uma opção adicional para um item, como 'extra queijo', 'pimenta', etc.
    """
    id_opcao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    itens = models.ManyToManyField(Item, related_name='opcoes', through='OpcaoItem')

    class Meta:
        managed = False
        db_table = 'opcao'

    def __str__(self):
        return self.nome


class OpcaoItem(models.Model):
    """
    Tabela intermediária para a relação entre Item e Opção.
    """
    id_opcao_item = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)

    class Meta:
        managed = False

    def __str__(self):
        return f"{self.item} - {self.opcao}"


class Menu(models.Model):
    """
    Representa um menu, que é composto por uma coleção de itens/produtos.
    """
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, primary_key=True, related_name='produto_menu')
    itens = models.ManyToManyField(Item, related_name='menus', through='MenuItem')

    class Meta:
        managed = False
        db_table = 'menu'

    def __str__(self):
        return self.produto.nome


class MenuItem(models.Model):
    """
    Tabela intermediária para a relação entre Menu e Item.
    """
    id_menu_item = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        managed = False

    def __str__(self):
        return f'{self.menu} - {self.item}'


class DiaSemana(models.Model):
    """
    Representa um dia da semana, para associar menus disponíveis em dias específicos.
    """
    id_dia_semana = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    menus = models.ManyToManyField(Menu, related_name='dias', through='MenuDiaSemana')

    class Meta:
        managed = False
        db_table = 'diasemana'

    def __str__(self):
        return self.nome


class MenuDiaSemana(models.Model):
    """
    Tabela intermediária para a relação entre Menu e DiaSemana, especificando a disponibilidade no almoço/jantar.
    """
    id_menu_dia_semana = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dia_semana = models.ForeignKey(DiaSemana, on_delete=models.CASCADE)
    almoco = models.BooleanField()  # Se o menu é válido para o almoço
    jantar = models.BooleanField()  # Se o menu é válido para o jantar

    class Meta:
        managed = False

    def __str__(self):
        return f'{self.menu} - {self.dia_semana} - Almoço: {self.almoco} - Jantar: {self.jantar}'
