from django.db import models

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True, unique=True)
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
        return self.nome

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True, unique=True)
    designacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias_view'

    def __str__(self):
        return self.designacao
    

class Tipos(models.Model):
    id_tipo = models.AutoField(primary_key=True, unique=True)
    designacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_view'

    def __str__(self):
        return self.designacao
    

class Opcoes(models.Model):
    id_opcao = models.AutoField(primary_key=True, unique=True)
    designacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'opcoes_view'

    def __str__(self):
        return self.designacao
    

class Itens(models.Model):
    id_item = models.OneToOneField(Produtos, on_delete=models.CASCADE, primary_key=True, unique=True, related_name='produto_item', db_column='id_item')
    categorias = models.ManyToManyField(Categorias, related_name='itens', through='itenscategorias')
    tipos = models.ManyToManyField(Tipos, related_name='itens', through='itenstipos')
    opcoes = models.ManyToManyField(Opcoes, related_name='itens', through='itensopcoes')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens_view'

    def __str__(self):
        return self.id_item.nome


class ItensCategorias(models.Model):
    id_item_categoria = models.AutoField(primary_key=True, unique=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, db_column='id_categoria')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itenscategorias'

    def __str__(self):
        return f'{self.id_item} - {self.id_categoria}'


class ItensTipos(models.Model):
    id_item_tipo = models.AutoField(primary_key=True, unique=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE, db_column='id_tipo')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itenstipos'

    def __str__(self):
        return f"Item: {self.id_item} - Tipo: {self.id_tipo}"
    

class ItensOpcoes(models.Model):
    id_item_opcao = models.AutoField(primary_key=True, unique=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_opcao = models.ForeignKey(Opcoes, on_delete=models.CASCADE, db_column='id_opcao')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itensopcoes'

    def __str__(self):
        return f"{self.id_item} - {self.id_opcao}"
    

class Menus(models.Model):
    id_menu = models.OneToOneField(Produtos, on_delete=models.CASCADE, primary_key=True, unique=True, related_name='produto_menu', db_column='id_menu')
    itens = models.ManyToManyField(Itens, related_name='menus', through='ItensMenus')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus_view'

    def __str__(self):
        return self.id_menu.nome


class ItensMenus(models.Model):
    id_item_menu = models.AutoField(primary_key=True, unique=True)
    id_item = models.ForeignKey(Itens, on_delete=models.CASCADE, db_column='id_item')
    id_menu = models.ForeignKey(Menus, on_delete=models.CASCADE, db_column='id_menu')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'itensmenus'

    def __str__(self):
        return f'Menu: {self.id_menu} - Item: {self.id_item}'


class DiasSemana(models.Model):
    id_dia_semana = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=50)
    menus = models.ManyToManyField(Menus, related_name='dias', through='MenusDiasSemana')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'diassemana'

    def __str__(self):
        return self.nome


class MenusDiasSemana(models.Model):
    id_menu_dia_semana = models.AutoField(primary_key=True, unique=True)
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
        return f'Menu: {self.id_menu} - Dia: {self.id_dia_semana} - Almoço: {self.almoco} - Jantar: {self.jantar}'
