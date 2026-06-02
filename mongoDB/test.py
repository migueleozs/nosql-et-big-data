from pymongo import MongoClient

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['packt']

dbname = get_database()
print(dbname)

collection = dbname["books"]
print(collection.count_documents({}))

items = collection.find()
for item in items:
    print(item['_id'], item['title'])