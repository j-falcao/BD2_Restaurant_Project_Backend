from .models import Ingrediente, Utensilio, Receita, Carrinho, Fornecedor


def get_all_ingredientes():
    return Ingrediente.objects.all()

def get_ingrediente_by_id(id_ingrediente):
    return Ingrediente.objects.get(id_ingrediente=id_ingrediente)


def get_all_utensilios():
    return Utensilio.objects.all()

def get_utensilio_by_id(id_utensilio):
    return Utensilio.objects.get(id_utensilio=id_utensilio)


def get_all_receitas():
    return Receita.objects.all()

def get_receita_by_id(id_receita):
    return Receita.objects.get(id_receita=id_receita)


def get_all_carrinhos():
    return Carrinho.objects.all()

def get_carrinho_by_id(id_carrinho):
    return Carrinho.objects.get(id_carrinho=id_carrinho)


def get_all_fornecedores():
    return Fornecedor.objects.all()

def get_fornecedor_by_id(id_fornecedor):
    return Fornecedor.objects.get(id_fornecedor=id_fornecedor)