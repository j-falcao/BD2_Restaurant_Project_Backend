from datetime import timedelta
import os
from django.core.management.base import BaseCommand
from faker import Faker
from tqdm import tqdm
from django.db import connection, transaction
from produtos import db as produtos_db
from pedidos import db as pedidos_db
from autenticacao import db as autenticacao_db
from django.db import connection, transaction
import random


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

        self.stdout.write(self.style.SUCCESS("Dropping views..."))
        self._run_sql_file(os.getcwd() + '/database/scripts/drop_views.sql')
        self.stdout.write(self.style.SUCCESS("Dropping tables..."))
        self._run_sql_file(os.getcwd() + '/database/scripts/drop_tables.sql')
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
            self.seed_produtos_itens_menus(num_entries)
            self.seed_tipos()
            self.seed_opcoes()
            self.seed_estados_mesas()
            self.seed_mesas(num_entries)
            self.seed_servicos(num_entries)  # ta errado, nao da para testar
            """ self.seed_reservas(num_entries) """
            self.seed_itens_opcoes(num_entries)
            self.seed_pedidos_produtos_itens_opcoes(num_entries)
            self.seed_categorias()
            self.seed_fornecedores(num_entries)
            self.seed_ingredientes(num_entries)
            self.seed_utensilios(num_entries)
            self.seed_receitas(num_entries)
            self.seed_dias_semana()
            self.seed_ingredientes_receitas(num_entries)
            self.seed_utensilios_receitas(num_entries)
            self.seed_instrucoes(num_entries)
            self.seed_instrucoes_ingredientes(num_entries)
            self.seed_menus_dias_semana(num_entries)
            self.seed_itens_categorias(num_entries)
            self.seed_itens_tipos(num_entries)
            self.stdout.write(self.style.SUCCESS("Data seeding completed successfully."))
        except Exception as e:
            transaction.rollback()
            self.stdout.write(self.style.ERROR(f"An error occurred during data seeding: {e}"))

    def seed_estados_mesas(self):
        estados_mesas = [
            "Ocupada",
            "Livre",
            "Reservada"
        ]
        with connection.cursor() as cursor:
            for estado_mesa in tqdm(estados_mesas, desc="Seeding estados_mesas"):
                cursor.execute("INSERT INTO estadosmesas(designacao) VALUES (%s)", [estado_mesa])
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
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding mesas"):
                id_estado_mesa = fake.random_int(min=1, max=3)
                numero = _ + 1
                capacidade_maxima = fake.random_int(min=2, max=12)
                quantidade_clientes = 0
                cursor.execute(
                    "INSERT INTO mesas(id_estado_mesa, numero, capacidade_maxima, quantidade_clientes) VALUES (%s, %s, %s, %s)",
                    [id_estado_mesa, numero, capacidade_maxima, quantidade_clientes]
                )


    def seed_produtos_itens_menus(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            for i in tqdm(range(num_entries), desc="Seeding produtos/itens/menus/itens_menus"):
                # Determine if it's an item or menu
                item = i > num_entries * 0.75  # 75% of products are items
                menu = not item

                # Generate product details
                nome = fake.word()
                url_imagem = fake.image_url()
                preco = fake.random_number(digits=5, fix_len=True) / 100

                # Insert into produtos table
                cursor.execute(
                    """
                    INSERT INTO produtos (item, menu, nome, url_imagem, preco)
                    VALUES (%s, %s, %s, %s, %s) RETURNING id_produto
                    """,
                    [item, menu, nome, url_imagem, preco]
                )
                id_produto = cursor.fetchone()[0]

                # If it's an item, insert into itens
                if item:
                    porcao_unidade_medida = fake.random_element(elements=['kg', 'g', 'ml', 'l', 'unidade'])
                    porcao = fake.random_int(min=1, max=100)
                    cursor.execute(
                        """
                        INSERT INTO itens (id_item, porcao_unidade_medida, porcao)
                        VALUES (%s, %s, %s)
                        """,
                        [id_produto, porcao_unidade_medida, porcao]
                    )

                # If it's a menu, insert into menus and itensmenus
                if menu:
                    cursor.execute(
                        """
                        INSERT INTO menus (id_menu) VALUES (%s)
                        RETURNING id_menu
                        """,
                        [id_produto]
                    )
                    id_menu = cursor.fetchone()[0] if cursor.rowcount > 0 else id_produto

                    # Fetch categories and randomly assign an item from each category
                    categorias = produtos_db.get_all_categorias()
                    for categoria in categorias:
                        # Get items for the category
                        itens = produtos_db.get_itens_by_categoria(categoria)
                        if itens:  # Ensure the list is not empty
                            random_item = random.choice(itens)  # Select a random item
                            cursor.execute(
                                """
                                INSERT INTO itensmenus (id_item, id_menu)
                                VALUES (%s, %s)
                                """,
                                [random_item, id_menu]
                            )



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
        with transaction.atomic(), connection.cursor() as cursor:
            for categoria in tqdm(categorias, desc="Seeding categorias"):
                cursor.execute(
                    "INSERT INTO categorias (designacao) VALUES (%s) ON CONFLICT DO NOTHING",
                    [categoria]
                )


    def seed_opcoes(self):
        opcoes = [
            "Gelo",
            "Molho",
            "Tempero especial",
            "Picante",
            "Extra queijo",
            "Extra pepino",
            "Extra berinjela",
        ]  
        with transaction.atomic(), connection.cursor() as cursor:
            for opcao in tqdm(opcoes, desc="Seeding opcoes"):
                cursor.execute(
                    "INSERT INTO opcoes(designacao) VALUES (%s)",
                    [opcao]
                )

    def seed_dias_semana(self):
        dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        with transaction.atomic(), connection.cursor() as cursor:
            for dia in tqdm(dias, desc="Seeding dias_semana"):
                cursor.execute("INSERT INTO diassemana(designacao) VALUES (%s)", [dia])

    def seed_ingredientes_receitas(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding ingredientes_receitas"):
                id_receita = fake.random_int(min=1, max=100) 
                id_ingrediente = fake.random_int(min=1, max=500) 
                cursor.execute(
                    "INSERT INTO ingredientesreceitas(id_receita, id_ingrediente) VALUES (%s, %s)",
                    [id_receita, id_ingrediente]
                )
            

    def seed_utensilios_receitas(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding utensilios_receitas"):
                id_receita = fake.random_int(min=1, max=100)  # IDs de receitas existentes
                id_utensilio = fake.random_int(min=1, max=300)  # IDs de utensílios existentes
                cursor.execute(
                    "INSERT INTO utensiliosreceitas(id_receita, id_utensilio) VALUES (%s, %s)",
                    [id_receita, id_utensilio]
                )

    def seed_instrucoes(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding instrucoes"):
                id_receita = fake.random_int(min=1, max=100)
                total_instrucoes = fake.random_int(min=3, max=10)
                for numero_sequencia in range(1, total_instrucoes + 1):
                    descricao = fake.sentence(nb_words=12) 
                    cursor.execute(
                        "INSERT INTO instrucoes (id_receita, numero_sequencia, descricao) VALUES (%s, %s, %s)",
                        [id_receita, numero_sequencia, descricao]
                    )

    def seed_instrucoes_ingredientes(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding instrucoesingredientes"):
                id_instrucao = fake.random_int(min=1, max=500)
                total_ingredientes = fake.random_int(min=1, max=5)
                for _ in range(total_ingredientes):
                    id_ingrediente = fake.random_int(min=1, max=1000)
                    cursor.execute(
                        "INSERT INTO instrucoesingredientes (id_instrucao, id_ingrediente) VALUES (%s, %s)",
                        [id_instrucao, id_ingrediente]
                    )

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
        with transaction.atomic(), connection.cursor() as cursor:
            for tipo in tqdm(tipos, desc="Seeding tipos"):
                cursor.execute(
                    "INSERT INTO tipos (designacao) VALUES (%s) ON CONFLICT DO NOTHING",
                    [tipo]
                )

    def seed_itens_tipos(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding itenstipos"):
                itens = produtos_db.get_all_itens()
                id_item = itens[fake.random_int(min=0, max=len(itens) - 1)].id_item_id
                id_tipo = fake.random_int(min=1, max=7)
                cursor.execute(
                    "INSERT INTO itenstipos (id_item, id_tipo) VALUES (%s, %s)",
                    [id_item, id_tipo]
                )
            
    def seed_itens_categorias(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in tqdm(range(num_entries), desc="Seeding itenscategorias"):
                itens = produtos_db.get_all_itens()
                id_item = itens[fake.random_int(min=0, max=len(itens) - 1)].id_item_id
                id_categoria = fake.random_int(min=1, max=7)
                cursor.execute(
                    "INSERT INTO itenscategorias (id_item, id_categoria) VALUES (%s, %s)",
                    [id_item, id_categoria]
                )

    def seed_itens_opcoes(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            itens = produtos_db.get_all_itens()
            id_itens = [item.id_item_id for item in itens]
            for _ in tqdm(range(num_entries), desc="Seeding itensopcoes"):
                id_item = fake.random_element(id_itens)
                id_opcao = fake.random_int(min=1, max=7)
                cursor.execute(
                    "INSERT INTO itensopcoes (id_item, id_opcao) VALUES (%s, %s)",
                    [id_item, id_opcao]
                )

    def seed_menus_dias_semana(self, num_entries):
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        
        with transaction.atomic(), connection.cursor() as cursor:
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

    def seed_servicos(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            id_garcons = [garcom.id_utilizador_id for garcom in autenticacao_db.get_all_garcons()]
            id_mesas = [mesa.id_mesa for mesa in pedidos_db.get_all_mesas()]
            for _ in tqdm(range(num_entries), desc="Seeding servicos"):
                id_mesa = fake.random_element(elements=id_mesas)
                id_garcom = fake.random_element(elements=id_garcons)
                data_hora_inicio = fake.date_time_this_year()
                data_hora_fim = data_hora_inicio + timedelta(minutes=fake.random_int(min=30, max=120))
                preco_total = fake.random_number(digits=3) + fake.random_int(min=10, max=30)

                cursor.execute(
                    """
                    INSERT INTO servicos (id_garcom, id_mesa, data_hora_inicio, data_hora_fim, preco_total)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id_servico
                    """,
                    [id_garcom, id_mesa, data_hora_inicio, data_hora_fim, preco_total]
                )
                id_servico = cursor.fetchone()[0]

                num_pedidos = fake.random_int(min=1, max=5)
                for _ in range(num_pedidos):
                    pedido_inicio = data_hora_inicio + timedelta(minutes=fake.random_int(min=5, max=30))
                    pedido_fim = pedido_inicio + timedelta(minutes=fake.random_int(min=10, max=30))
                    cursor.execute(
                        """
                        INSERT INTO pedidos (id_servico, data_hora_inicio, data_hora_fim)
                        VALUES (%s, %s, %s)
                        RETURNING id_pedido
                        """,
                        [id_servico, pedido_inicio, pedido_fim]
                    )
                    id_pedido = cursor.fetchone()[0]

                    num_produtos = fake.random_int(min=1, max=5)
                    id_produto = [produto.id_produto_id for produto in produtos_db.get_all_produtos()]
                    id_cozinheiro = [cozinheiro.id_cozinheiro_id for cozinheiro in autenticacao_db.get_all_cozinheiros()]
                    for _ in range(num_produtos):
                        cursor.execute(
                            """
                            INSERT INTO pedidosprodutos (id_pedido, id_produto, id_cozinheiro)
                            VALUES (%s, %s, %s)
                            """,
                            [id_pedido, id_produto, id_cozinheiro]
                        )

    def seed_pedidos_produtos_itens_opcoes(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            pedidosprodutos = pedidos_db.get_all_pedidos_produtos()
            id_pedidosprodutos = [pedido_produto.id_pedido_produto for pedido_produto in pedidosprodutos]

            
            itensopcoes = produtos_db.get_all_itens_opcoes()
            id_itensopcoes = [item_opcao.id_item_opcao for item_opcao in itensopcoes]

            for _ in tqdm(range(num_entries), desc="Seeding pedidosprodutositensopcoes"):
                id_pedido_produto = fake.random_element(elements=id_pedidosprodutos)
                id_item_opcao = fake.random_element(elements=id_itensopcoes)
                
                cursor.execute(
                    "INSERT INTO pedidosprodutositensopcoes (id_item_opcao, id_pedido_produto) VALUES (%s, %s)",
                    [id_item_opcao, id_pedido_produto]
                )

    def seed_reservas(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            id_mesas = [mesa.id_mesa for mesa in pedidos_db.get_all_mesas()]
            id_servicos = [servico.id_servico for servico in pedidos_db.get_all_servicos()]

            print(id_mesas)
            print(id_servicos)

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