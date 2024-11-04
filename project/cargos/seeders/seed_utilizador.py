from cargos.models import Utilizador, Turno

def run():
    utilizadores_data = [
        {
            "username": "josem",
            "primeiro_nome": "José",
            "ultimo_nome": "Martins",
            "morada": "Rua Principal 123",
            "telefone": "912345678",
            "email": "jose@example.com",
            "data_nascimento": "1985-05-20",
            "genero": "Masculino",
            "turno": Turno.objects.get(nome="Manhã")
        },
        {
            "username": "mariag",
            "primeiro_nome": "Maria",
            "ultimo_nome": "Gomes",
            "morada": "Avenida Secundária 456",
            "telefone": "913456789",
            "email": "maria@example.com",
            "data_nascimento": "1990-08-15",
            "genero": "Feminino",
            "turno": Turno.objects.get(nome="Tarde")
        }
    ]
    for utilizador_data in utilizadores_data:
        utilizador, created = Utilizador.objects.get_or_create(**utilizador_data)
        if created:
            print(f"Utilizador {utilizador.username} criado")
        else:
            print(f"Utilizador {utilizador.username} já existe")
