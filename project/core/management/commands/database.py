from datetime import datetime, timedelta
import os
from django.core.management.base import BaseCommand
from faker import Faker
from django.db import connection, transaction
from autenticacao.utils import hash_password
from produtos.models import *
from servicos.models import *
from autenticacao.models import *
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

        self.stdout.write(self.style.SUCCESS("Revoking privileges..."))
        self._run_sql_file(os.getcwd() + '/core/bd/revoke_privileges.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/revoke_privileges.sql')
        self.stdout.write(self.style.SUCCESS("Dropping triggers..."))
        self._run_sql_file(os.getcwd() + '/core/bd/drop_triggers_updated_at.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/drop_triggers.sql')
        self._run_sql_file(os.getcwd() + '/servicos/bd/drop_triggers.sql')
        self.stdout.write(self.style.SUCCESS("Dropping stored procedures..."))
        self._run_sql_file(os.getcwd() + '/autenticacao/bd/drop_stored_procedures.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/drop_stored_procedures.sql')
        self._run_sql_file(os.getcwd() + '/produtos/bd/drop_stored_procedures.sql')
        self._run_sql_file(os.getcwd() + '/servicos/bd/drop_stored_procedures.sql')
        # self.stdout.write(self.style.SUCCESS("Dropping indexes..."))
        # self._run_sql_file(os.getcwd() + '/inventario/bd/drop_indexes.sql')
        self.stdout.write(self.style.SUCCESS("Dropping views..."))
        self._run_sql_file(os.getcwd() + '/autenticacao/bd/drop_views.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/drop_views.sql')
        self._run_sql_file(os.getcwd() + '/produtos/bd/drop_views.sql')
        self._run_sql_file(os.getcwd() + '/servicos/bd/drop_views.sql')
        self.stdout.write(self.style.SUCCESS("Dropping tables..."))
        self._run_sql_file(os.getcwd() + '/servicos/bd/drop_tables.sql')
        self._run_sql_file(os.getcwd() + '/produtos/bd/drop_tables.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/drop_tables.sql')
        self._run_sql_file(os.getcwd() + '/autenticacao/bd/drop_tables.sql')
        self.stdout.write(self.style.SUCCESS("Dropping roles..."))
        self._run_sql_file(os.getcwd() + '/core/bd/drop_roles.sql')

        self.stdout.write(self.style.SUCCESS("Creating roles..."))
        self._run_sql_file(os.getcwd() + '/core/bd/create_roles.sql')
        self.stdout.write(self.style.SUCCESS("Creating tables..."))
        self._run_sql_file(os.getcwd() + '/autenticacao/bd/create_tables.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/create_tables.sql')
        self._run_sql_file(os.getcwd() + '/produtos/bd/create_tables.sql')
        self._run_sql_file(os.getcwd() + '/servicos/bd/create_tables.sql')
        self.stdout.write(self.style.SUCCESS("Creating views..."))
        self._run_sql_file(os.getcwd() + '/autenticacao/bd/create_views.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/create_views.sql')
        self._run_sql_file(os.getcwd() + '/produtos/bd/create_views.sql')
        self._run_sql_file(os.getcwd() + '/servicos/bd/create_views.sql')
        self.stdout.write(self.style.SUCCESS("Creating indexes..."))
        self._run_sql_file(os.getcwd() + '/inventario/bd/create_indexes.sql')
        self.stdout.write(self.style.SUCCESS("Creating stored procedures..."))
        self._run_sql_file(os.getcwd() + '/autenticacao/bd/create_stored_procedures.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/create_stored_procedures.sql')
        self._run_sql_file(os.getcwd() + '/produtos/bd/create_stored_procedures.sql')
        self._run_sql_file(os.getcwd() + '/servicos/bd/create_stored_procedures.sql')
        self.stdout.write(self.style.SUCCESS("Creating triggers..."))
        self._run_sql_file(os.getcwd() + '/core/bd/create_triggers_updated_at.sql')
        self._run_sql_file(os.getcwd() + '/inventario/bd/create_triggers.sql')
        self._run_sql_file(os.getcwd() + '/servicos/bd/create_triggers.sql')
        self.stdout.write(self.style.SUCCESS("Granting privileges..."))
        self._run_sql_file(os.getcwd() + '/inventario/bd/grant_privileges.sql')

        self._seed_all()

    def _seed_all(self):
        num_entries = 10000
        self.stdout.write(self.style.WARNING(f"Seeding..."))
        try:
            self.stdout.write(self.style.SUCCESS("Seeding cargos"))
            self.seed_cargos()

            self.stdout.write(self.style.SUCCESS("Seeding utilizadores"))
            self.seed_utilizadores()

            self.stdout.write(self.style.SUCCESS("Seeding fornecedores"))
            self.seed_fornecedores(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding ingredientes"))
            self.seed_ingredientes(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding utensilios"))
            self.seed_utensilios(num_entries)
            
            self.stdout.write(self.style.SUCCESS("Seeding tiposcarrinhos"))
            self.seed_tiposcarrinhos()

            self.stdout.write(self.style.SUCCESS("Seeding carrinhos"))
            self.seed_carrinhos()

            self.stdout.write(self.style.SUCCESS("Seeding produtos/itens/itens_menus"))
            self.seed_produtos_itens_menus(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding receitas"))
            self.seed_receitas(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding tipos"))
            self.seed_tipos()

            self.stdout.write(self.style.SUCCESS("Seeding categorias"))
            self.seed_categorias()

            self.stdout.write(self.style.SUCCESS("Seeding opcoes"))
            self.seed_opcoes()

            self.stdout.write(self.style.SUCCESS("Seeding itenscategorias"))
            self.seed_itenscategorias(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding itenstipos"))
            self.seed_itenstipos(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding itensopcoes"))
            self.seed_itensopcoes(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding diassemana"))
            self.seed_diassemana()

            self.stdout.write(self.style.SUCCESS("Seeding menusdiassemana"))
            self.seed_menusdiassemana(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding estadosmesas"))
            self.seed_estadosmesas()

            self.stdout.write(self.style.SUCCESS("Seeding mesas"))
            self.seed_mesas(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding estadospedidosprodutos"))
            self.seed_estadospedidosprodutos()

            # self.stdout.write(self.style.SUCCESS("Seeding servicos/pedidos/pedidosprodutos"))
            # self.seed_servicos_pedidos_pedidosprodutos(num_entries)

            self.stdout.write(self.style.SUCCESS("Seeding estadosreservas"))
            self.seed_estadosreservas()

            # self.stdout.write(self.style.SUCCESS("Seeding reservas"))
            # self.seed_reservas(num_entries)

            self.stdout.write(self.style.SUCCESS("Data seeding completed successfully."))
        except Exception as e:
            transaction.rollback()
            self.stdout.write(self.style.ERROR(f"An error occurred during data seeding: {e}"))

    def seed_cargos(self):
        cargos = [
            "Administrador",
            "Cozinheiro",
            "Garcom",
        ]
        with connection.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO cargos(designacao) VALUES (%s) ON CONFLICT DO NOTHING",
                [(cargo,) for cargo in cargos]
            )

    def seed_utilizadores(self):
        utilizadores_data = []
        for _ in range(10):
            id_cargo = 1 if _ == 0 else random.randint(1, 3)
            first_name = fake.first_name()
            last_name = fake.last_name()
            is_superuser = _ == 0
            username = 'dev' if _ == 0 else fake.user_name()
            url_imagem = fake.image_url(width=400, height=300)
            raw_password = 'password' if _ == 0 else fake.password()
            password_hash = hash_password(raw_password)  # Hash the password
            utilizadores_data.append((
                id_cargo, first_name, last_name, is_superuser, username, url_imagem,
                password_hash
            ))

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                """
                INSERT INTO utilizadores(
                    id_cargo, first_name, last_name, is_superuser, username, url_imagem, password
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                utilizadores_data
            )

    def seed_fornecedores(self, num_entries):
        fornecedores_data = []
        for _ in range(num_entries):
            nome = fake.company()
            vende_ingredientes = fake.boolean()
            vende_utensilios = not vende_ingredientes
            morada = fake.address()
            email = fake.email()
            telemovel = fake.phone_number()
            fornecedores_data.append((nome, vende_ingredientes, vende_utensilios, morada, email, telemovel))

        with connection.cursor() as cursor:
            cursor.executemany(
                """
                INSERT INTO fornecedores(
                    nome, vende_ingredientes, vende_utensilios, morada, email, telemovel
                ) VALUES (%s, %s, %s, %s, %s, %s)
                """,
                fornecedores_data
            )

    def seed_ingredientes(self, num_entries):
        ingredientes_data = []
        for _ in range(num_entries):
            id_fornecedor = fake.random_int(min=1, max=100)
            nome = fake.word()
            url_imagem = fake.image_url(width=400, height=300)
            quantidade_stock = fake.random_int(min=1, max=1000)
            unidade_medida = fake.random_element(elements=['kg', 'g', 'ml', 'l', 'unidade'])
            limite_stock = fake.random_int(min=100, max=2000)
            preco = fake.random_number(digits=4, fix_len=True) / 100
            ingredientes_data.append((id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco))

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                """
                INSERT INTO ingredientes(
                    id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                ingredientes_data
            )

    def seed_utensilios(self, num_entries):
        utensilios_data = []
        for _ in range(num_entries):
            id_fornecedor = fake.random_int(min=1, max=100)
            nome = fake.word()
            url_imagem = fake.image_url(width=400, height=300)
            quantidade_stock = fake.random_int(min=1, max=1000)
            unidade_medida = fake.random_element(elements=['kg', 'g', 'ml', 'l', 'unidade'])
            limite_stock = fake.random_int(min=100, max=2000)
            preco = fake.random_number(digits=4, fix_len=True) / 100
            utensilios_data.append((id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco))

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                """
                INSERT INTO utensilios (id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                utensilios_data
            )

    def seed_tiposcarrinhos(self):
        tipos = [
            "Ingredientes",
            "Utensilios"
        ]
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                """
                INSERT INTO tiposcarrinhos (designacao) VALUES (%s)
                """,
                [(tipo,) for tipo in tipos]
            )


    def seed_carrinhos(self):
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO carrinhos (preco_total, id_tipo_carrinho, data_compra) VALUES (%s, %s, %s)", (0, 1, None)
            )
            cursor.execute(
                "INSERT INTO carrinhos (preco_total, id_tipo_carrinho, data_compra) VALUES (%s, %s, %s)", (0, 2, None)
            )

    def seed_estadosmesas(self):
        data = [
            "Disponivel",
            "Ocupada",
            "Reservada",
        ]
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
            "INSERT INTO estadosmesas (designacao) VALUES (%s)", [(estado,) for estado in data]
        )

    def seed_mesas(self, num_entries):
        data = [
            (
                fake.random_int(min=2, max=12),
            )
            for i in range(num_entries)
        ]
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
            "INSERT INTO mesas (capacidade_maxima) VALUES (%s)",
            data,
        )

    def seed_produtos_itens_menus(self, num_entries):
        produtos_data = []
        itens_data = []
        menus_data = []
        itensmenus_data = []

        categorias = Categorias.fetch_all()

        for i in range(num_entries):
            item = i > num_entries * 0.75
            menu = not item
            
            nome = fake.word()
            url_imagem = fake.image_url(width=400, height=300)
            preco = fake.random_number(digits=5, fix_len=True) / 100

            produtos_data.append((item, menu, nome, url_imagem, preco))


        with connection.cursor() as cursor:
            query = """
            INSERT INTO produtos (item, menu, nome, url_imagem, preco)
            VALUES %s RETURNING id_produto
            """
            values = ", ".join(
                cursor.mogrify("(%s, %s, %s, %s, %s)", data).decode('utf-8')
                for data in produtos_data
            )
            cursor.execute(query % values)
            ids = [row[0] for row in cursor.fetchall()]

        for i, id_produto in enumerate(ids):
            if produtos_data[i][0]:  # If item
                itens_data.append(
                    (
                        id_produto,
                        fake.random_element(elements=["kg", "g", "ml", "l", "unidade"]),
                        fake.random_int(min=1, max=100),
                    )
                )
            else:  # If menu
                menus_data.append((id_produto,))
                for categoria in categorias:
                    itens = ItensCategorias.fetch_by_categoria(categoria['id_categoria'])
                    if itens:
                        random_item = random.choice(itens)
                        itensmenus_data.append((random_item['id_item'], id_produto))

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO itens (id_item, porcao_unidade_medida, porcao) VALUES (%s, %s, %s)",
                itens_data,
            )
            cursor.executemany(
                "INSERT INTO menus (id_menu) VALUES (%s)", menus_data
            )
            cursor.executemany(
                "INSERT INTO itensmenus (id_item, id_menu) VALUES (%s, %s)", itensmenus_data
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
        data = [(categoria,) for categoria in categorias]
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO categorias(designacao) VALUES(%s)",
                data,
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
        data = [(opcao,) for opcao in opcoes]
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO opcoes (designacao) VALUES (%s)", data
            )

    def seed_diassemana(self):
        dias = [
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
            "Domingo",
        ]
        data = [(dia,) for dia in dias]
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO diassemana (designacao) VALUES (%s)", data
            )

    def seed_receitas(self, num_receitas, max_ingredientes=5, max_utensilios=3, max_instrucoes=10):
        ingredientes = []
        utensilios = []
        instrucoes = []
        produtos = [ item['id_item'] for item in Itens.fetch_all()]
        
        with transaction.atomic(), connection.cursor() as cursor:
            for _ in range(num_receitas):
                nome = fake.word()
                duracao = f"{fake.random_int(min=1, max=300)} minutes"
                produto = random.choice(produtos)
                cursor.execute("INSERT INTO receitas (nome, duracao, id_produto) VALUES (%s, %s, %s) RETURNING id_receita", (nome, duracao, produto))
                id_receita = cursor.fetchone()[0]
                
                num_ingredientes = fake.random_int(min=1, max=max_ingredientes)
                for _ in range(num_ingredientes):
                    ingredientes.append((id_receita, fake.random_int(min=1, max=500), fake.random_int(min=1, max=100)))
        
                num_utensilios = fake.random_int(min=1, max=max_utensilios)
                for _ in range(num_utensilios):
                    utensilios.append((id_receita, fake.random_int(min=1, max=10000), fake.random_int(min=1, max=100)))
        
                num_instrucoes = fake.random_int(min=3, max=max_instrucoes)
                for numero_sequencia in range(1, num_instrucoes + 1):
                    instrucoes.append((id_receita, numero_sequencia, fake.sentence(nb_words=12)))
        
            if ingredientes:
                cursor.executemany("INSERT INTO ingredientesreceitas (id_receita, id_ingrediente, quantidade) VALUES (%s, %s, %s)", ingredientes)
            if utensilios:
                cursor.executemany("INSERT INTO utensiliosreceitas (id_receita, id_utensilio, quantidade) VALUES (%s, %s, %s)", utensilios)
            if instrucoes:
                cursor.executemany("INSERT INTO instrucoes (id_receita, numero_sequencia, descricao) VALUES (%s, %s, %s)", instrucoes)

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
            cursor.executemany(
                "INSERT INTO tipos (designacao) VALUES (%s) ON CONFLICT DO NOTHING",
                [(tipo,) for tipo in tipos]
            )

    def seed_generic_table(self, table_name, columns, data):
        placeholders = ", ".join(["%s"] * len(columns))
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(query, data)

    def seed_itenstipos(self, num_entries):
        itens = Itens.fetch_all()
        data = [
            (itens[fake.random_int(min=0, max=len(itens) - 1)]['id_item'], fake.random_int(min=1, max=7))
            for _ in range(num_entries)
        ]

        self.seed_generic_table("itenstipos", ["id_item", "id_tipo"], data)

    def seed_itenscategorias(self, num_entries):
        itens = Itens.fetch_all()
        data = [
            (itens[fake.random_int(min=0, max=len(itens) - 1)]['id_item'], fake.random_int(min=1, max=7))
            for _ in range(num_entries)
        ]

        self.seed_generic_table("itenscategorias", ["id_item", "id_categoria"], data)

    def seed_itensopcoes(self, num_entries):
        itens = Itens.fetch_all()
        id_itens = [item['id_item'] for item in itens]
        data = [
            (fake.random_element(id_itens), fake.random_int(min=1, max=7))
            for _ in range(num_entries)
        ]

        self.seed_generic_table("itensopcoes", ["id_item", "id_opcao"], data)

    def seed_menusdiassemana(self, num_entries):
        dias_semana = [
            "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
            "Sexta-feira", "Sábado", "Domingo"
        ]
        data = [
            (
                fake.random_int(min=1, max=100),  # id_menu
                dias_semana.index(fake.random_element(dias_semana)) + 1,  # id_dia_semana
                fake.boolean(),
                fake.boolean()
            )
            for _ in range(num_entries)
        ]

        self.seed_generic_table(
            "menusdiassemana", ["id_menu", "id_dia_semana", "almoco", "jantar"], data
        )

    def seed_estadospedidosprodutos(self):
        data = [
            "Pendente",
            "Preparando",
            "Pronto",
        ]

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO estadospedidosprodutos (designacao) VALUES (%s)", [(estado,) for estado in data]
            )

    def seed_servicos_pedidos_pedidosprodutos(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            id_garcons = [int(garcom["id"]) for garcom in Utilizadores.fetch_all_garcons()]
            id_mesas = [int(mesa["id_mesa"]) for mesa in Mesas.fetch_disponiveis()]

            servicos_ids = []
            pedidos_data = []

            for _ in range(num_entries):
                id_mesa = fake.random_element(elements=id_mesas)
                id_garcom = fake.random_element(elements=id_garcons)
                data_hora_fim = datetime.now() + timedelta(minutes=fake.random_int(min=30, max=120))
                preco_total = fake.random_int(min=10, max=100)

                cursor.execute(
                    "INSERT INTO servicos (id_garcom, id_mesa, data_hora_fim, preco_total) VALUES (%s, %s, %s, %s) RETURNING id_servico",
                    (id_garcom, id_mesa, data_hora_fim, preco_total),
                )
                servicos_ids.append(cursor.fetchone()[0])

            for id_servico in servicos_ids:
                num_pedidos = fake.random_int(min=1, max=5)
                pedidos_data.extend([(id_servico,) for _ in range(num_pedidos)])

            pedidos_ids = []
            for data in pedidos_data:
                cursor.execute(
                    "INSERT INTO pedidos (id_servico) VALUES (%s) RETURNING id_pedido",
                    data,
                )
                pedidos_ids.append(cursor.fetchone()[0])

            # for id_pedido in pedidos_ids:
            #     num_produtos = fake.random_int(min=1, max=5)
            #     pedidosprodutos_data.extend(
            #         [
            #             (
            #                 id_pedido,
            #                 fake.random_element(elements=id_produtos),
            #                 fake.random_element(elements=id_cozinheiros),
            #             )
            #             for _ in range(num_produtos)
            #         ]
            #     )
            
            # cursor.executemany(
            #     "INSERT INTO pedidosprodutos (id_pedido, id_produto, id_cozinheiro) VALUES (%s, %s, %s)",
            #     pedidosprodutos_data,
            # )



    def seed_estadosreservas(self):
        with transaction.atomic(), connection.cursor() as cursor:
            data = [
                ('Confirmada',), 
                ('Concluida',),
                ('Cancelada',)
            ]
            cursor.executemany(
                "INSERT INTO estadosreservas (designacao) VALUES (%s)",
                data
            )

    def seed_reservas(self, num_entries):
        with transaction.atomic(), connection.cursor() as cursor:
            id_mesas = [mesa['id_mesa'] for mesa in Mesas.fetch_all()]
            id_estadosreservas = [estado['id_estado_reserva'] for estado in EstadosReservas.fetch_all()]
            id_garcons = [garcom['id_utilizador'] for garcom in Utilizadores.fetch_all_garcons()]

            reservas_data = [
                (
                    fake.random_element(elements=id_mesas), # mesa
                    fake.random_element(elements=id_estadosreservas), # estado
                    fake.random_int(min=1), # quantidade_pessoas
                    fake.catch_phrase(), # Observacoes
                    fake.random_element(elements=id_garcons), # garcom que fez a reserva
                    fake.date_time_this_year(), # data_hora
                    fake.random_int(min=30, max=120), # minutos_antes
                    fake.random_int(min=30, max=120), # minutos_depois
                )
                for _ in range(num_entries)
            ]

            cursor.executemany(
                """
                INSERT INTO reservas (id_mesa, id_estado_reserva, quantidade_pessoas, id_garcom, observacoes, data_hora, minutos_antes, minutos_depois)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                reservas_data
            )
