# Generated by Django 5.1.2 on 2024-11-30 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pedidosprodutos',
            table='pedidosprodutos',
        ),
        migrations.AlterModelTable(
            name='pedidosprodutositensopcoes',
            table='pedidosprodutositensopcoes',
        ),
    ]
