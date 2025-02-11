import pymongo
from pymongo import MongoClient
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
database = client["BD2_Projeto"]


## INVENTARIO
def create_ingrediente(ingrediente):
    collection = database["inventarios"]
    collection.insert_one({**ingrediente})

def create_utensilio(utensilios_data): # tipo de utensilio mais comum
    collection = database["inventarios"]
    collection.insert_one({**utensilios_data})

def update_ingrediente(id_ingrediente, quantidade):
    collection = database["inventarios"]
    collection.update_one({"id_ingrediente": id_ingrediente}, {"$set": {"quantidade_stock": quantidade}})

def update_utensilio(id_utensilio, quantidade):
    collection = database["inventarios"]
    collection.update_one({"id_utensilio": id_utensilio}, {"$set": {"quantidade_stock": quantidade}})

def create_ingredienteCarrinho(ingredienteCarrinho_data): # quantidade de ingredientes por carrinho, admnistrador com mais adicoes de ingredientes
    collection = database["carrinho"]
    collection.insert_one({**ingredienteCarrinho_data})

def create_utensilioCarrinho(utensilioCarrinho_data): # quantidade de utensilios por carrinho, admnistrador com mais adicoes de utensilios
    collection = database["carrinho"]
    collection.insert_one({**utensilioCarrinho_data})


## PRODUTOS
def create_item(itens_data):
    collection = database["produtos"]   
    collection.insert_one({**itens_data, "tipos": [], "categorias": [], "opcoes": []})

def update_item(item):
    collection = database["produtos"]
    collection.update_one({"id_item": item['id_item']}, {"$set": {**item}})

def delete_item(id_item):
    collection = database["produtos"]
    collection.delete_one({"id_item": id_item})

def create_tipo(tipo):
    collection = database["tipos"]
    collection.insert_one({**tipo})

def update_tipo(tipo):
    collection = database["tipos"]
    collection.update_one({"id_tipo": tipo['id_tipo']}, {"$set": {**tipo}})

def delete_tipo(id_tipo):
    collection = database["tipos"]
    collection.delete_one({"id_tipo": id_tipo})

def create_itemtipo(itemtipo):
    collection = database["produtos"]
    collection.update_one(
        {"id_item": itemtipo['id_item']}, 
        {"$addToSet": {"tipos": itemtipo['id_tipo']}}
    )

def delete_itemtipo(itemtipo):
    collection = database["produtos"]
    collection.update_one(
        {"id_item": itemtipo["id_item"]}, 
        {"$pull": {"tipos": itemtipo["id_tipo"]}}
    )


def create_categoria(categoria):
    collection = database["categorias"]
    collection.insert_one({**categoria})

def update_categoria(categoria):
    collection = database["categorias"]
    collection.update_one({"id_categoria": categoria['id_categoria']}, {"$set": {**categoria}})

def delete_categoria(id_categoria):
    collection = database["categorias"]
    collection.delete_one({"id_categoria": id_categoria})

def create_itemcategoria(itemcategoria):
    collection = database["produtos"]
    collection.update_one(
        {"id_item": itemcategoria['id_item']}, 
        {"$addToSet": {"categorias": itemcategoria['id_categoria']}}
    )

def delete_itemcategoria(itemcategoria):
    collection = database["produtos"]
    collection.update_one(
        {"id_item": itemcategoria["id_item"]}, 
        {"$pull": {"categorias": itemcategoria["id_categoria"]}}
    )


def create_opcao(opcao):
    collection = database["opcoes"]
    collection.insert_one({**opcao})

def update_opcao(opcao):
    collection = database["opcoes"]
    collection.update_one({"id_opcao": opcao['id_opcao']}, {"$set": {**opcao}})

def delete_opcao(id_opcao):
    collection = database["opcoes"]
    collection.delete_one({"id_opcao": id_opcao})

def create_itemopcao(itemopcao):
    collection = database["produtos"]
    collection.update_one(
        {"id_item": itemopcao['id_item']}, 
        {"$addToSet": {"opcoes": itemopcao['id_opcao']}}
    )

def delete_itemopcao(itemopcao):
    collection = database["produtos"]
    collection.update_one(
        {"id_item": itemopcao["id_item"]}, 
        {"$pull": {"opcoes": itemopcao["id_opcao"]}}
    )


def create_menu(menus_data): # preco medio, dia da semana com mais menus
    collection = database["produtos"]   
    collection.insert_one({**menus_data})

def update_menu(menu):
    collection = database["produtos"]
    collection.update_one({"id_menu": menu['id_menu']}, {"$set": {**menu}})

def delete_menu(id_menu):
    collection = database["produtos"]
    collection.delete_one({"id_menu": id_menu})

def create_itemmenu(itemmenus_data):
    collection = database["produtos"]   
    collection.insert_one({**itemmenus_data})

def delete_itemmenu(itemmenu):
    collection = database["produtos"]
    collection.delete_one({"id_item": itemmenu["id_item"]})

def tipos_itens_mais_usados():
    collection = database["inventarios"]
    return collection.aggregate([{"$group": {"_id": "$id_item", "quantidade": {"$sum": 1}}}, {"$sort": {"quantidade": -1}}])

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