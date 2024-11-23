import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from faker import Faker
from tqdm import tqdm
from django.db import connection, transaction

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with fake data or manage tables using stored procedures.'

    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true', help='Reset the database by dropping and creating tables, stored procedures, views, and seeding data.')
        parser.add_argument('--file', type=str, help='Path to an SQL file to run for seeding.')
        parser.add_argument('--seed', action='store_true', help='Generate and insert fake data into all tables.')

    def handle(self, *args, **options):
        if options['file']:
            self._run_sql_file(options['file'])

        if options['seed']:
            self._seed_all()

        if options['reset']:
            self._reset_db()


    def _run_sql_file(self, file_path):
        if not os.path.isfile(file_path):
            self.stdout.write(self.style.ERROR(f"File {file_path} does not exist."))
            return

        try:
            with open(file_path, 'r') as f:
                sql = f.read()
            with connection.cursor() as cursor:
                cursor.execute(sql)
                transaction.commit()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))

    def _reset_db(self):
        self.stdout.write(self.style.WARNING("Resetting the database..."))

        self.stdout.write(self.style.SUCCESS("Dropping tables..."))
        self._run_sql_file(os.getcwd() + '/database/scripts/drop_tables.sql')
        # self.stdout.write(self.style.SUCCESS("Dropping views..."))
        # self._run_sql_file(os.getcwd() + '/database/scripts/drop_views.sql')
        # self.stdout.write(self.style.SUCCESS("Dropping stored procedures..."))
        # self._run_sql_file(os.getcwd() + '/database/scripts/drop_stored_procedures.sql')

        self.stdout.write(self.style.SUCCESS("Creating tables..."))
        self._run_sql_file(os.getcwd() + '/database/scripts/create_tables.sql')
        # self.stdout.write(self.style.SUCCESS("Creating views..."))
        # self._run_sql_file(os.getcwd() + '/database/scripts/create_views.sql')
        # self.stdout.write(self.style.SUCCESS("Creating stored procedures..."))
        # self._run_sql_file(os.getcwd() + '/database/scripts/create_stored_procedures.sql')

        # Seed the database
        self._seed_all()

    def _seed_all(self):
        num_entries = 10000
        self.stdout.write(self.style.WARNING(f"Seeding..."))
        try:
            self.seed_estados_mesas(num_entries)
            self.seed_fornecedores(num_entries)
            self.seed_carrinhos(num_entries)
            self.seed_ingredientes(num_entries)
            self.seed_utensilios(num_entries)
            self.seed_receitas(num_entries)
            self.seed_mesas(num_entries)
            self.seed_produtos(num_entries)
            self.seed_categorias(num_entries)
            self.seed_opcoes(num_entries)
            self.seed_menus(num_entries)
            self.seed_dias_semana(num_entries)
            self.stdout.write(self.style.SUCCESS("Data seeding completed successfully."))
        except Exception as e:
            transaction.rollback()
            self.stdout.write(self.style.ERROR(f"An error occurred during data seeding: {e}"))

    def seed_estados_mesas(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding estados_mesas"):
                designacao = fake.word()
                cursor.execute("INSERT INTO estadosmesas(designacao) VALUES (%s)", [designacao])
            transaction.commit()

    def seed_fornecedores(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding fornecedores"):
                nome = fake.company()
                vende_ingredientes = fake.boolean()
                vende_utensilios = not vende_ingredientes
                morada = fake.address()
                email = fake.email()
                telemovel = fake.phone_number()
                cursor.execute(
                    "INSERT INTO fornecedores(nome, vende_ingredientes, vende_utensilios, morada, email, telemovel) VALUES (%s, %s, %s, %s, %s, %s)",
                    [nome, vende_ingredientes, vende_utensilios, morada, email, telemovel]
                )
            transaction.commit()

    def seed_carrinhos(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding carrinhos"):
                preco_total = fake.random_number(digits=5)
                data_compra = fake.date_time_this_year()
                cursor.execute("INSERT INTO carrinhos(preco_total, data_compra) VALUES (%s, %s)", [preco_total, data_compra])
            transaction.commit()

    def seed_ingredientes(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding ingredientes"):
                id_fornecedor = fake.random_int(min=1, max=100)
                nome = fake.word()
                url_imagem = fake.image_url()
                quantidade_stock = fake.random_int(min=1, max=1000)
                unidade_medida = fake.random_element(elements=['kg', 'g', 'ml', 'l', 'unidade'])
                limite_stock = fake.random_int(min=100, max=2000)
                preco = fake.random_number(digits=4, fix_len=True) / 100
                cursor.execute(
                    "INSERT INTO ingredientes(id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    [id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco]
                )
            transaction.commit()

    def seed_utensilios(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding utensilios"):
                id_fornecedor = fake.random_int(min=1, max=100)
                nome = fake.word()
                quantidade_stock = fake.random_int(min=1, max=500)
                limite_stock = fake.random_int(min=100, max=2000)
                preco = fake.random_number(digits=4, fix_len=True) / 100
                cursor.execute(
                    "INSERT INTO utensilios(id_fornecedor, nome, quantidade_stock, limite_stock, preco) VALUES (%s, %s, %s, %s, %s)",
                    [id_fornecedor, nome, quantidade_stock, limite_stock, preco]
                )
            transaction.commit()

    def seed_receitas(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding receitas"):
                nome = fake.word()
                # Generate a random duration as an interval string
                duracao_minutes = fake.random_int(min=1, max=300)  # Duration in minutes (1-300 minutes)
                duracao_interval = f"{duracao_minutes} minutes"
                cursor.execute(
                    "INSERT INTO receitas(nome, duracao) VALUES (%s, %s)",
                    [nome, duracao_interval]
                )
            transaction.commit()

    def seed_mesas(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding mesas"):
                id_estado_mesa = fake.random_int(min=1, max=10)
                numero = fake.random_int(min=1, max=50)
                capacidade_maxima = fake.random_int(min=2, max=12)
                quantidade_clientes = 0
                cursor.execute(
                    "INSERT INTO mesas(id_estado_mesa, numero, capacidade_maxima, quantidade_clientes) VALUES (%s, %s, %s, %s)",
                    [id_estado_mesa, numero, capacidade_maxima, quantidade_clientes]
                )
            transaction.commit()

    def seed_produtos(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding produtos"):
                item = fake.boolean()
                menu = not item
                nome = fake.word()
                url_imagem = fake.image_url()
                preco = fake.random_number(digits=5, fix_len=True) / 100
                cursor.execute(
                    "INSERT INTO produtos(item, menu, nome, url_imagem, preco) VALUES (%s, %s, %s, %s, %s)",
                    [item, menu, nome, url_imagem, preco]
                )
            transaction.commit()

    def seed_categorias(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding categorias"):
                designacao = fake.word()
                cursor.execute("INSERT INTO categorias(designacao) VALUES (%s)", [designacao])
            transaction.commit()

    def seed_opcoes(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding opcoes"):
                designacao = fake.word()
                cursor.execute(
                    "INSERT INTO opcoes(designacao) VALUES (%s)",
                    [designacao]
                )
            transaction.commit()

    def seed_menus(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding menus"):
                cursor.execute(
                    "INSERT INTO menus VALUES ()",
                    []
                )
            transaction.commit()

    def seed_dias_semana(self, num_entries):
        dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        with connection.cursor() as cursor:
            for dia in tqdm(dias, desc="Seeding dias_semana"):
                cursor.execute("INSERT INTO dias_semana(nome) VALUES (%s)", [dia])
            transaction.commit()