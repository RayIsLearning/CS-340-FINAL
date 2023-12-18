from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:56101/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

# Method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            print('Nothing to save, because data parameter is empty')
            return False

# Method to implement the R in CRUD
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            print('Nothing to read, because data parameter is empty')
            return False

# Method to implement the U in CRUD
    def update(self, data, change):
        if data is not None:
            return self.database.animals.update(data,{ "$set": change})  
	# data and change are dictionaries
        else:
            print('Nothing to update, because data parameter is empty')
            return False

# Method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data)  # data is dictionary
        else:
            print('Nothing to delete, because data parameter is empty')
            return False