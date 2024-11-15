import os
from django.core.management.base import BaseCommand
from faker import Faker
from tqdm import tqdm
from django.db import connection, transaction

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with fake data or manage tables using stored procedures.'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to an SQL file to run for seeding.')

        parser.add_argument('--create-tables', action='store_true', help='Run stored procedure to create tables.')
        parser.add_argument('--drop-tables', action='store_true', help='Run stored procedure to drop tables.')

        parser.add_argument('--seed', help='Generate and insert fake data into tables.')

        parser.add_argument('--create-views', action='store_true', help='Run stored procedure to create views.')
        parser.add_argument('--drop-views', action='store_true', help='Run stored procedure to drop views.')

        parser.add_argument('--create-stored-procedures', action='store_true', help='Run stored procedure to create stored procedures.')
        parser.add_argument('--drop-stored-procedures', action='store_true', help='Run stored procedure to drop stored procedures.')

        parser.add_argument('--reset-db', action='store_true', help='Reset the database by dropping and creating tables, stored procedures, views, running seeders, etc...')

    def handle(self, *args, **options):
        if options['file']:
            self._run_sql_file(options['file'])

        if options['create_tables']:
            self._run_sql_file(os.getcwd() + '/database/scripts/create_tables.sql')
        if options['drop_tables']:
            self._run_sql_file(os.getcwd() + '/database/scripts/drop_tables.sql')

        if options['seed']:
            self._seed_data()

        if options['create_views']:
            self._run_sql_file(os.getcwd() + '/database/scripts/create_views.sql')
        if options['drop_views']:
            self._run_sql_file(os.getcwd() + '/database/scripts/drop_views.sql')

        if options['create_stored_procedures']:
            self._run_sql_file(os.getcwd() + '/database/scripts/create_stored_procedures.sql')
        if options['drop_stored_procedures']:
            self._run_sql_file(os.getcwd() + '/database/scripts/drop_stored_procedures.sql')

        if(options['reset_db']):
            self._reset_db()

        self.stdout.write(self.style.SUCCESS("Database management completed successfully."))

    def _run_sql_file(self, file_path):
        if not os.path.isfile(file_path):
            self.stdout.write(self.style.ERROR(f"File {file_path} does not exist."))
            return

        self.stdout.write(self.style.WARNING(f"Running SQL file: {file_path}"))
        try:
            with open(file_path, 'r') as f:
                sql = f.read()
            with connection.cursor() as cursor:
                cursor.execute(sql)
                transaction.commit()
            self.stdout.write(self.style.SUCCESS("SQL file executed successfully."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))

    def _execute_stored_procedure(self, procedure_name):
        self.stdout.write(self.style.WARNING(f"Executing stored procedure: {procedure_name}"))
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"CALL {procedure_name}()")  # Use CALL instead of SELECT
                transaction.c_run_sql_fileommit()
            self.stdout.write(self.style.SUCCESS(f"Stored procedure {procedure_name} executed successfully."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while executing {procedure_name}: {e}"))

    def _seed_data(self):
        num_entries = 10000
        self.stdout.write(self.style.WARNING(f"Seeding {num_entries} entries for each table..."))

        with connection.cursor() as cursor:
            try:
                for _ in tqdm(range(num_entries), desc="Seeding produtos"):
                    item, menu, nome, url_imagem, preco = True, False, fake.name(), fake.url(), fake.random_number(digits=5)
                    cursor.execute("INSERT INTO Produto(item, menu, nome, url_imagem, preco) VALUES (%s, %s, %s, %s, %s)", [item, menu, nome, url_imagem, preco])

                transaction.commit()
                self.stdout.write(self.style.SUCCESS(f"Data seeding completed successfully for {num_entries} entries per table."))

            except Exception as e:
                transaction.rollback()
                self.stdout.write(self.style.ERROR(f"An error occurred during data seeding: {e}"))

    def _reset_db(self):
        # drop
        self._run_sql_file(os.getcwd() + '/project/database/scripts/drop_tables.sql')
        self._run_sql_file(os.getcwd() + '/project/database/scripts/drop_views.sql')
        self._run_sql_file(os.getcwd() + '/project/database/scripts/drop_stored_procedures.sql')

        # create
        self._run_sql_file(os.getcwd() + '/project/database/scripts/create_tables.sql')
        self._run_sql_file(os.getcwd() + '/project/database/scripts/create_views.sql')
        self._run_sql_file(os.getcwd() + '/project/database/scripts/create_stored_procedures.sql')

        # seed
        self._seed_data()