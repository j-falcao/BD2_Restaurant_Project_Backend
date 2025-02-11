from pymongo import MongoClient
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
database = client["BD2_Projeto"]


## INVENTARIO
def create_ingrediente(ingrediente):
    collection = database["inventario"]
    collection.insert_one({**ingrediente})

def create_utensilio(utensilios_data):
    collection = database["inventario"]
    collection.insert_one({**utensilios_data})

def update_ingrediente(id_ingrediente, quantidade):
    collection = database["inventario"]
    collection.update_one({"id_ingrediente": id_ingrediente}, {"$set": {"quantidade_stock": quantidade}})

def update_utensilio(id_utensilio, quantidade):
    collection = database["inventario"]
    collection.update_one({"id_utensilio": id_utensilio}, {"$set": {"quantidade_stock": quantidade}})


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



# ANALISE
def percentagem_ingredientes_por_tipo():
    collection = database["inventario"]

    # pipeline = [
    #     {"$unwind": "$tipos"},
    #     {"$group": {
    #         "_id": "$tipos",
    #         "count": {"$sum": 1}
    #     }},
    #     {"$group": {
    #         "_id": None,
    #         "total": {"$sum": "$count"},
    #         "types": {"$push": {"id_tipo": "$_id", "count": "$count"}}
    #     }},
    #     {"$unwind": "$types"},
    #     {"$addFields": {
    #         "types.percentage": {
    #             "$multiply": [
    #                 {"$divide": ["$types.count", "$total"]},
    #                 100
    #             ]
    #         }
    #     }},
    #     {"$project": {
    #         "_id": 0,
    #         "id_tipo": "$types.id_tipo",
    #         "count": "$types.count",
    #         "percentage": "$types.percentage"
    #     }},
    #     {"$lookup": {
    #         "from": "tipos",
    #         "localField": "id_tipo",
    #         "foreignField": "_id",
    #         "as": "tipo_info"
    #     }},
    #     {"$unwind": "$tipo_info"},
    #     {"$project": {
    #         "id_tipo": 1,
    #         "tipo_name": "$tipo_info.name",
    #         "count": 1,
    #         "percentage": 1
    #     }}
    # ]

    # result = list(collection.aggregate(pipeline))

    total_ingredientes = collection.count_documents({})

    if total_ingredientes == 0:
        return {}
    
    pipeline = [
        {"$unwind": "$tipos"},  # Expande o array de tipos
        {"$group": {"_id": "$tipos", "count": {"$sum": 1}}},  # Conta ingredientes por tipo
        {
            "$project": {
                "_id": 0,
                "id_tipo": "$_id",
                "percentagem": {"$multiply": [{"$divide": ["$count", total_ingredientes]}, 100]},
            }
        }
    ]

    resultados = list(collection.aggregate(pipeline))

    return resultados
