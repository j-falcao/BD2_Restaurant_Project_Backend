from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    URL_Image = models.CharField(max_length=100)
    preco = models.FloatField()

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.nome
    
class Menu(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return self.descricao
    
class MenuItem(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='menu_items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        db_table = 'menu_item'

    def __str__(self):
        return f"Item {self.item.nome} no Menu {self.menu.descricao}"

class Item(models.Model):
    nome = models.CharField(max_length=100)  # Adicionando nome para identificação
    quantidade = models.IntegerField()
    unidade_medida = models.CharField(max_length=100)

    class Meta:
        db_table = 'item'

    def __str__(self):
        return f"{self.nome} - {self.quantidade} {self.unidade_medida}"
