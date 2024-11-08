from cargos.models import Turno

def run():
    turnos_data = [
        {"nome": "Manhã", "hora_inicio": "08:00:00", "hora_fim": "12:00:00"},
        {"nome": "Tarde", "hora_inicio": "13:00:00", "hora_fim": "17:00:00"},
        {"nome": "Noite", "hora_inicio": "18:00:00", "hora_fim": "22:00:00"},
    ]
    for turno_data in turnos_data:
        turno, created = Turno.objects.get_or_create(**turno_data)
        if created:
            print(f"Turno {turno.nome} criado")
        else:
            print(f"Turno {turno.nome} já existe")
