from .serializers import *
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from . import db

@api_view(['GET', 'POST'])
def get_post_ingredientes(request):
    print('ooalaolaoaloa')

    if request.method == 'GET':
        # Check if query parameter 'id_ingrediente' is present
        id_ingrediente = request.GET.get('id_ingrediente')
        
        if id_ingrediente:
            # Fetch a single ingredient by ID
            try:
                ingrediente = db.get_ingrediente_by_id(id_ingrediente)
                serializer = IngredientesSerializer(ingrediente)
                return JsonResponse(serializer.data, safe=False)
            except Ingredientes.DoesNotExist:
                raise Http404("Ingrediente not found")
        else:
            # Fetch all ingredients
            ingredientes = db.get_all_ingredientes()
            serializer = IngredientesSerializer(ingredientes, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # Create a new ingredient
        serializer = IngredientesSerializer(data=request.data)
        if serializer.is_valid():
            db.create_ingrediente(serializer.validated_data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@api_view(['PUT', 'DELETE'])
def update_delete_ingredientes(request, id_ingrediente):
    if request.method == 'PUT':
        # Update an existing ingredient
        try:
            ingrediente = db.get_ingrediente_by_id(id_ingrediente)
            serializer = IngredientesSerializer(ingrediente, data=request.data)
            if serializer.is_valid():
                db.update_ingrediente(serializer.validated_data)
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        except Ingredientes.DoesNotExist:
            raise Http404("Ingrediente not found")
    elif request.method == 'DELETE':
        # Delete an ingredient
        try:
            ingrediente = db.get_ingrediente_by_id(id_ingrediente)
            db.delete_ingrediente(ingrediente)
            return JsonResponse({"message": "Ingrediente deleted successfully"}, status=200)
        except Ingredientes.DoesNotExist:
            raise Http404("Ingrediente not found")

@api_view(['GET']) # ✅
def get_utensilios(request):
    utensilios = db.get_all_utensilios()
    serializer = UtensiliosSerializer(utensilios, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET']) # ✅
def get_utensilio(request, id_utensilio):
    utensilio = db.get_utensilio_by_id(id_utensilio)
    serializer = UtensiliosSerializer(utensilio)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_receitas(request):
    receitas = db.get_all_receitas()
    serializer = ReceitasSerializer(receitas, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_receita(request, id_receita):
    print('OOOOOOOOOOOOOOOOOOO')
    receita = db.get_receita_by_id(id_receita)
    serializer = ReceitasSerializer(receita)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_carrinhos(request):
    carrinhos = db.get_all_carrinhos()
    serializer = CarrinhosSerializer(carrinhos, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_carrinho(request, id_carrinho):
    carrinho = db.get_carrinho_by_id(id_carrinho)
    serializer = CarrinhosSerializer(carrinho)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_fornecedores(request):
    fornecedores = db.get_all_fornecedores()
    serializer = FornecedoresSerializer(fornecedores, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_fornecedor(request, id_fornecedor):
    fornecedor = db.get_fornecedor_by_id(id_fornecedor)
    serializer = FornecedoresSerializer(fornecedor)
    return JsonResponse(serializer.data, safe=False)