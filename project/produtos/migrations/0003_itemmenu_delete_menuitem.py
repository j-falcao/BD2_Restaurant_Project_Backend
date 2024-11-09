# Generated by Django 5.1.2 on 2024-11-09 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_itemopcao_delete_opcaoitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('id_item_menu', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'menuitem',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
