# Generated by Django 4.1.13 on 2024-10-18 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('id_diaSemana', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id_opcao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.BooleanField()),
                ('menu', models.BooleanField()),
                ('nome', models.CharField(max_length=100)),
                ('url_imagem', models.URLField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='produto_item', serialize=False, to='produtos.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='produto_menu', serialize=False, to='produtos.produto')),
            ],
        ),
        migrations.CreateModel(
            name='OpcaoItem',
            fields=[
                ('id_opcaoItem', models.AutoField(primary_key=True, serialize=False)),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.opcao')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.item')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id_menuItem', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.item')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.menu')),
            ],
        ),
        migrations.CreateModel(
            name='MenuDiaSemana',
            fields=[
                ('id_menu_diaSemana', models.AutoField(primary_key=True, serialize=False)),
                ('almoco', models.BooleanField()),
                ('jantar', models.BooleanField()),
                ('diaSemana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.diasemana')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.menu')),
            ],
        ),
        migrations.CreateModel(
            name='ItemTipo',
            fields=[
                ('id_itemTipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.tipo')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategoria',
            fields=[
                ('id_itemCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.item')),
            ],
        ),
    ]
