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
        parser.add_argument('--create', action='store_true', help='Run stored procedure to create tables.')
        parser.add_argument('--drop', action='store_true', help='Run stored procedure to drop tables.')
        parser.add_argument('--seed', action='store_true', help='Generate and insert fake data into tables.')

    def handle(self, *args, **options):
        if options['file']:
            self._run_sql_file(options['file'])

        if options['create']:
            self._execute_stored_procedure('create_tabelas')

        if options['drop']:
            self._execute_stored_procedure('drop_tabelas')

        if options['seed']:
            self._seed_data()

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
                transaction.commit()
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
