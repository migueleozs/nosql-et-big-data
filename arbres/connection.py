from pymongo import MongoClient

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['arbre']

dbname = get_database()
print(dbname)

collection = dbname["arbre"]
print(collection.count_documents({}))

# ###
# items = collection.find(
#     {"commune": "CHATILLON"}, #lo que queremos encontrar
#     {"_id": 0, "commune": 1, "nom": 1} #lo que queremos mostrar
# )

# for item in items:
#     print(item['commune'], item['nom'])

# hauteur_20m = collection.find(
#     {"hauteur": {"$gt": 20}}, #lo que queremos encontrar
#     {"_id": 0, "hauteur": 1, "nom": 1} #lo que queremos mostrar
# )

# for item in hauteur_20m:
#     print(item['hauteur'], item['nom'])

# nom_contient_Chene = collection.find(
#     {"nom": {"$regex": "Chêne"}}, #lo que queremos encontrar
#     {"_id": 0, "nom": 1} #lo que queremos mostrar
# )

# for item in nom_contient_Chene:
#     print(item['nom'])


arbres_plus_hautes = collection.find(
    {}, #lo que queremos encontrar
    {"_id": 0, "hauteur": 1, "nom": 1} #lo que queremos mostrar
).sort("hauteur", -1) #ordenar por altura descendente

for item in arbres_plus_hautes.limit(10): #limitar a los 10 primeros
     print(item['nom'], item['hauteur'])
###

arbres_avec_circonference = collection.find(
    #{"circonference": {"$exists": True}}, #lo que queremos encontrar
    {"circonference": {"$gt": 300}}, #lo que queremos encontrar
    {"_id": 0, "circonference": 1, "nom": 1} #lo que queremos mostrar
)

for item in arbres_avec_circonference:
    print(item['nom'], item['circonference'])