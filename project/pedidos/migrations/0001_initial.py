# Generated by Django 5.1.2 on 2024-11-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosMesas',
            fields=[
                ('id_estado_mesa', models.AutoField(primary_key=True, serialize=False)),
                ('designacao', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'estadosmesas_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mesas',
            fields=[
                ('id_mesa', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('capacidade_maxima', models.IntegerField()),
                ('quantidade_ocupantes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'mesas_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'pedidos_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PedidosProdutos',
            fields=[
                ('id_pedido_produto', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'pedidosprodutos_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PedidosProdutosItensOpcoes',
            fields=[
                ('id_pedido_produto_item_opcao', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'pedidosprodutositensopcoes_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('minutos_antes', models.DurationField()),
                ('minutos_depois', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'reservas_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id_servico', models.AutoField(primary_key=True, serialize=False)),
                ('data_hora_inicio', models.DateTimeField(auto_now_add=True)),
                ('data_hora_fim', models.DateTimeField(blank=True, null=True)),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'servicos_view',
                'managed': False,
            },
        ),
    ]
