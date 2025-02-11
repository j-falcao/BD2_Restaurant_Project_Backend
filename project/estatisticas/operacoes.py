import pymongo
from pymongo import MongoClient
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
database = client["BD2_Projeto"]


## INVENTARIO
def create_ingrediente(ingrediente_data): # preco medio e fornecedor com mais ingredientes
    collection = database["inventario"]
    collection.insert_one({**ingrediente_data})

def create_utensilio(utensilio_data): # preco medio e fornecedor com mais utensilios
    collection = database["inventario"]
    collection.insert_one({**utensilio_data})

def create_ingredienteCarrinho(ingredienteCarrinho_data): # quantidade de ingredientes por carrinho, admnistrador com mais adicoes de ingredientes
    collection = database["carrinho"]
    collection.insert_one({**ingredienteCarrinho_data})

def create_utensilioCarrinho(utensilioCarrinho_data): # quantidade de utensilios por carrinho, admnistrador com mais adicoes de utensilios
    collection = database["carrinho"]
    collection.insert_one({**utensilioCarrinho_data})


## PRODUTOS
def create_receita(receitas_data): # duracao media
    collection = database["produtos"]   
    collection.insert_one({**receitas_data})

def create_item(itens_data): # preco medio, tipo de item mais comum, categoria de item mais comum
    collection = database["produtos"]   
    collection.insert_one({**itens_data})

def create_itemmenu(itemmenus_data): # itens mais usados em menus
    collection = database["produtos"]   
    collection.insert_one({**itemmenus_data})

def create_menu(menus_data): # preco medio, dia da semana com mais menus
    collection = database["produtos"]   
    collection.insert_one({**menus_data})


## SERVICOS
def create_reserva(reservas_data): # mesas com mais reservas
    collection = database["reservas"]   
    collection.insert_one({**reservas_data})

def create_servico(servicos_data): # duracao media, preco medio
    collection = database["servicos"]   
    collection.insert_one({**servicos_data})

## UTILIZADORES
def create_utilizador(utilizadores_data): # cargo mais comum
    collection = database["utilizadores"]   
    collection.insert_one({**utilizadores_data})