import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from faker import Faker
from tqdm import tqdm
from django.db import connection, transaction
from datetime import timedelta
from produtos import db

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
        self.stdout.write(self.style.SUCCESS("Dropping views..."))
        self._run_sql_file(os.getcwd() + '/database/scripts/drop_views.sql')
        # self.stdout.write(self.style.SUCCESS("Dropping stored procedures..."))
        # self._run_sql_file(os.getcwd() + '/database/scripts/drop_stored_procedures.sql')

        self.stdout.write(self.style.SUCCESS("Creating tables..."))
        self._run_sql_file(os.getcwd() + '/database/scripts/create_tables.sql')
        self.stdout.write(self.style.SUCCESS("Creating views..."))
        self._run_sql_file(os.getcwd() + '/database/scripts/create_views.sql')
        # self.stdout.write(self.style.SUCCESS("Creating stored procedures..."))
        # self._run_sql_file(os.getcwd() + '/database/scripts/create_stored_procedures.sql')

        # Seed the database
        self._seed_all()

    def _seed_all(self):
        num_entries = 10000
        self.stdout.write(self.style.WARNING(f"Seeding..."))
        try:
            self.seed_produtos(num_entries)
            self.seed_tipos()
            self.seed_categorias()
            self.seed_opcoes()
            self.seed_itens_tipos(num_entries)
            self.seed_itens_categorias(num_entries)
            self.sedd_itens_opcoes(num_entries)
            self.seed_estados_mesas(num_entries)
            self.seed_fornecedores(num_entries)
            self.seed_ingredientes(num_entries)
            self.seed_utensilios(num_entries)
            self.seed_receitas(num_entries)
            self.seed_mesas(num_entries)
            self.seed_dias_semana()
            self.seed_ingredientes_receitas(num_entries)
            self.seed_utensilios_receitas(num_entries)
            self.seed_instrucoes(num_entries)
            self.seed_instrucoes_ingredientes(num_entries)
            """ self.seed_itens_menus(num_entries) 
            self.seed_menus_dias_semana(num_entries)
            self.seed_pedidos_produtos_itens_opcoes(num_entries)
            self.seed_reservas(num_entries)
            self.seed_servicos(num_entries) """
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

    """     def seed_carrinhos(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding carrinhos"):
                preco_total = fake.random_number(digits=5)
                data_compra = fake.date_time_this_year()
                cursor.execute("INSERT INTO carrinhos(preco_total, data_compra) VALUES (%s, %s)", [preco_total, data_compra])
            transaction.commit() """

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
                    "INSERT INTO produtos (item, menu, nome, url_imagem, preco) VALUES (%s, %s, %s, %s, %s) RETURNING id_produto",
                    [item, menu, nome, url_imagem, preco]
                )
                id_produto = cursor.fetchone()[0]
                
                if item:
                    porcao_unidade_medida = fake.random_element(elements=['kg', 'g', 'ml', 'l', 'unidade'])
                    porcao = fake.random_int(min=1, max=100)
                    cursor.execute(
                        "INSERT INTO itens (id_item, porcao_unidade_medida, porcao) VALUES (%s, %s, %s)",
                        [id_produto, porcao_unidade_medida, porcao]
                    )
                
                if menu:
                    cursor.execute(
                        "INSERT INTO menus (id_menu) VALUES (%s) ON CONFLICT DO NOTHING",
                        [id_produto]
                    )
            transaction.commit()


    def seed_categorias(self):
        categorias = [
            "Alcoólicas",
            "Refrigerantes",
            "Vinhos",
            "Vegetarianos",
            "Sem Glúten",
            "Sem Lactose",
            "Picante",
        ]
        with connection.cursor() as cursor:
            for categoria in tqdm(categorias, desc="Seeding categorias"):
                cursor.execute(
                    "INSERT INTO categorias (designacao) VALUES (%s) ON CONFLICT DO NOTHING",
                    [categoria]
                )
            transaction.commit()


    def seed_opcoes(self):
        opcoes = [
            "Com gelo",
            "Sem gelo",
            "Com molho",
            "Sem molho",
            "Sem Lactose",
            "Com Picante",
            "Sem Picante",
        ]  
        with connection.cursor() as cursor:
            for opcao in tqdm(opcoes, desc="Seeding opcoes"):
                cursor.execute(
                    "INSERT INTO opcoes(designacao) VALUES (%s)",
                    [opcao]
                )
            transaction.commit()

    def seed_dias_semana(self):
        dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        with connection.cursor() as cursor:
            for dia in tqdm(dias, desc="Seeding dias_semana"):
                cursor.execute("INSERT INTO diassemana(designacao) VALUES (%s)", [dia])
            transaction.commit()

    def seed_ingredientes_receitas(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding ingredientes_receitas"):
                id_receita = fake.random_int(min=1, max=100) 
                id_ingrediente = fake.random_int(min=1, max=500) 
                cursor.execute(
                    "INSERT INTO ingredientesreceitas(id_receita, id_ingrediente) VALUES (%s, %s)",
                    [id_receita, id_ingrediente]
                )
            transaction.commit()

    def seed_utensilios_receitas(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding utensilios_receitas"):
                id_receita = fake.random_int(min=1, max=100)  # IDs de receitas existentes
                id_utensilio = fake.random_int(min=1, max=300)  # IDs de utensílios existentes
                cursor.execute(
                    "INSERT INTO utensiliosreceitas(id_receita, id_utensilio) VALUES (%s, %s)",
                    [id_receita, id_utensilio]
                )
            transaction.commit()

    def seed_instrucoes(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding instrucoes"):
                id_receita = fake.random_int(min=1, max=100)
                total_instrucoes = fake.random_int(min=3, max=10)
                for numero_sequencia in range(1, total_instrucoes + 1):
                    descricao = fake.sentence(nb_words=12) 
                    cursor.execute(
                        "INSERT INTO instrucoes (id_receita, numero_sequencia, descricao) VALUES (%s, %s, %s)",
                        [id_receita, numero_sequencia, descricao]
                    )
            transaction.commit()

    def seed_instrucoes_ingredientes(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding instrucoesingredientes"):
                id_instrucao = fake.random_int(min=1, max=500)
                total_ingredientes = fake.random_int(min=1, max=5)
                for _ in range(total_ingredientes):
                    id_ingrediente = fake.random_int(min=1, max=1000)
                    cursor.execute(
                        "INSERT INTO instrucoesingredientes (id_instrucao, id_ingrediente) VALUES (%s, %s)",
                        [id_instrucao, id_ingrediente]
                    )
            transaction.commit()

    def seed_tipos(self):
        tipos = [
            "Bebida",
            "Prato Principal",
            "Acompanhamento",
            "Sobremesa",
            "Entrada",
            "Lanche",
            "Molho",
        ]
        with connection.cursor() as cursor:
            for tipo in tqdm(tipos, desc="Seeding tipos"):
                cursor.execute(
                    "INSERT INTO tipos (designacao) VALUES (%s) ON CONFLICT DO NOTHING",
                    [tipo]
                )
            transaction.commit()

    def seed_itens_tipos(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding itenstipos"):
                itens = db.get_all_itens()
                id_item = itens[fake.random_int(min=0, max=len(itens) - 1)].id_item
                id_tipo = fake.random_int(min=0, max=6)
                cursor.execute(
                    "INSERT INTO itenstipos (id_item, id_tipo) VALUES (%s, %s)",
                    [id_item, id_tipo]
                )
            transaction.commit()

    def seed_itens_categorias(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding itenscategorias"):
                itens = db.get_all_itens()
                id_item = itens[fake.random_int(min=0, max=len(itens) - 1)].id_item
                id_categoria = fake.random_int(min=0, max=6)
                cursor.execute(
                    "INSERT INTO itenscategorias (id_item, id_categoria) VALUES (%s, %s)",
                    [id_item, id_categoria]
                )
            transaction.commit()

    def seed_itens_opcoes(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding itensopcoes"):
                itens = db.get_all_itens()
                id_item = itens[fake.random_int(min=0, max=len(itens) - 1)].id_item
                id_opcao = fake.random_int(min=0, max=6)
                cursor.execute(
                    "INSERT INTO itensopcoes (id_item, id_opcao) VALUES (%s, %s)",
                    [id_item, id_opcao]
                )
            transaction.commit()

    def seed_itens_menus(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding itensmenus"):
                id_menu = fake.random_int(min=1, max=100)
                id_item = fake.random_int(min=1, max=500)
                cursor.execute(
                    "INSERT INTO itensmenus (id_item, id_menu) VALUES (%s, %s)",
                    [id_item, id_menu]
                )
            transaction.commit()

    def seed_menus_dias_semana(self, num_entries):
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding menusdiassemana"):
                id_menu = fake.random_int(min=1, max=100)            
                dia_semana = fake.random_element(elements=dias_semana)            
                id_dia_semana = dias_semana.index(dia_semana) + 1
                almoco = fake.boolean()
                jantar = fake.boolean()
                
                cursor.execute(
                    "INSERT INTO menusdiassemana (id_menu, id_dia_semana, almoco, jantar) VALUES (%s, %s, %s, %s)",
                    [id_menu, id_dia_semana, almoco, jantar]
                )
            transaction.commit()

    """ def seed_servicos(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding servicos"):
                id_garcom = fake.random_int(min=1, max=100)
                id_mesa = fake.random_int(min=1, max=50)
                data_hora_inicio = fake.date_time_this_year()
                data_hora_fim = data_hora_inicio + timedelta(minutes=fake.random_int(min=30, max=120))
                preco_total = fake.random_number(digits=3) + fake.random_int(min=10, max=30)

                cursor.execute(
                    "INSERT INTO servicos (id_garcom, id_mesa, data_hora_inicio, data_hora_fim, preco_total) VALUES (%s, %s, %s, %s, %s)",
                    [id_garcom, id_mesa, data_hora_inicio, data_hora_fim, preco_total]
                )
                
                id_servico = cursor.lastrowid
                num_pedidos = fake.random_int(min=1, max=5)
                
                for _ in range(num_pedidos):
                    pedido_inicio = data_hora_inicio + timedelta(minutes=fake.random_int(min=5, max=30))
                    pedido_fim = pedido_inicio + timedelta(minutes=fake.random_int(min=10, max=30))
                    cursor.execute(
                        "INSERT INTO pedidos (id_servico, data_hora_inicio, data_hora_fim) VALUES (%s, %s, %s)",
                        [id_servico, pedido_inicio, pedido_fim]
                    )
                    
            transaction.commit()

    def seed_pedidos(self, num_entries):
        with connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding pedidos"):
                # Seleciona um serviço existente
                id_servico = fake.random_int(min=1, max=100)  # IDs de serviços existentes
                
                # Gera um número aleatório de pedidos para o serviço (1 a 5 pedidos)
                num_pedidos = fake.random_int(min=1, max=5)
                
                for _ in range(num_pedidos):
                    # Insere um pedido para o serviço
                    cursor.execute(
                        "INSERT INTO pedidos (id_servico) VALUES (%s)",
                        [id_servico]
                    )
            transaction.commit()
 """

    def seed_pedidos_produtos_itens_opcoes(self, num_entries):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_pedido_produto FROM pedidosprodutos")
            id_pedidosprodutos = [row[0] for row in cursor.fetchall()]
            
            cursor.execute("SELECT id_item_opcao FROM itensopcoes")
            id_itensopcoes = [row[0] for row in cursor.fetchall()]

            for _ in tqdm(range(num_entries), desc="Seeding pedidosprodutositensopcoes"):
                id_pedido_produto = fake.random_element(elements=id_pedidosprodutos)
                id_item_opcao = fake.random_element(elements=id_itensopcoes)
                
                cursor.execute(
                    "INSERT INTO pedidosprodutositensopcoes (id_item_opcao, id_pedido_produto) VALUES (%s, %s)",
                    [id_item_opcao, id_pedido_produto]
                )
            transaction.commit()

    def seed_reservas(self, num_entries):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_mesa FROM mesas")
            id_mesas = [row[0] for row in cursor.fetchall()]

            cursor.execute("SELECT id_servico FROM servicos")
            id_servicos = [row[0] for row in cursor.fetchall()]

            for _ in tqdm(range(num_entries), desc="Seeding reservas"):
                id_mesa = fake.random_element(elements=id_mesas)
                id_servico = fake.random_element(elements=id_servicos)
                data_hora = fake.date_time_this_year()
                minutos_antes = fake.random_int(min=0, max=120) 
                minutos_depois = fake.random_int(min=0, max=120)

                cursor.execute(
                    "INSERT INTO reservas (id_mesa, data_hora, minutos_antes, minutos_depois, id_servico) VALUES (%s, %s, %s, %s, %s)",
                    [id_mesa, data_hora, f"{minutos_antes} minutes", f"{minutos_depois} minutes", id_servico]
                )
            transaction.commit()