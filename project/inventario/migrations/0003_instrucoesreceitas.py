# Generated by Django 5.1.2 on 2024-11-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_carrinhos_fornecedores_ingredientes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrucoesReceitas',
            fields=[
                ('id_instrucao_receita', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
