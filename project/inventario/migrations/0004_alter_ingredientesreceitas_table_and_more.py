# Generated by Django 5.1.2 on 2024-11-14 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_instrucoesreceitas'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ingredientesreceitas',
            table='ingredientesreceitas_view',
        ),
        migrations.AlterModelTable(
            name='instrucoesreceitas',
            table='instrucoesreceitas_view',
        ),
        migrations.AlterModelTable(
            name='utensiliosreceitas',
            table='utensiliosreceitas_view',
        ),
    ]
