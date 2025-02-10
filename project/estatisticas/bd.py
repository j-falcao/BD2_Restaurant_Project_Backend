import pymongo
from pymongo import MongoClient

def dashboard():
    try:
        uri = "mongodb://localhost:27017/"
        client = MongoClient(uri)

        database = client["BD2_Projeto"]
        collection = database["estatisticas_inventario"]

        # start example code here
        collection.insert_one({"nome": "Maria", "idade": 20, "sexo": "F"})
        # end example code here

        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
