from rest_framework.response import Response
from rest_framework.decorators import api_view
import db


@api_view(['GET'])
def get_igredients(request):
    return Response(db.get_all_ingredientes())

@api_view(['GET'])
def get_ingrediente(request, id_ingrediente):
    return Response(db.get_ingrediente_by_id(id_ingrediente))

@api_view(['GET'])
def get_utensilios(request):
    return Response(db.get_all_utensilios())

@api_view(['GET'])
def get_utensilio(request, id_utensilio):
    return Response(db.get_utensilio_by_id(id_utensilio))


def get_receita_by_id(request, id_receita):
    return Response(db.get_receita_by_id(id_receita))

def get_receita_by_item(request, id_item):
    return Response(db.get_receita_by_item(id_item))

