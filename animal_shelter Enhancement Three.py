from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    #Mod 5 Added error handling so that if the connection fails the app will not crash
    def __init__(self, username, password):
    try:
        self.client = MongoClient(
            f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:32759/AAC?authSource=aac'
        )
        self.database = self.client['AAC']
        # Test connection
        self.client.admin.command('ping')
        print("MongoDB connection successful")
    except ConnectionFailure as e:
        raise ConnectionError(f"Could not connect to MongoDB: {e}")

# Complete this create method to implement the C in CRUD
    #  C in CRUD
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  
            if insert.acknowledged:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Complete this create method to implement the R in CRUD
#Mod 5 added sorting
    def read(self, query, projection=None, limit=0, sort=None):
    cursor = self.database.animals.find(query, projection)
    
    if sort:
        cursor = cursor.sort(sort)
    if limit:
        cursor = cursor.limit(limit)
        
    return list(cursor)
 # U in CRUD
    def update(self, query, new_values):
        if query and new_values:
            update_result = self.database.animals.update_many(query, {"$set": new_values})
            return update_result.modified_count
        else:
            raise Exception("Query and new values cannot be empty")
        
 # D in CRUD
    
    def delete(self, query):
        if query:
            delete_result = self.database.animals.delete_many(query)
            return delete_result.deleted_count
        else:
            raise Exception("Query cannot be empty")
