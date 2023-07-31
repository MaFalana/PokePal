'''
Name: db.py
Description: Database connection manager for
'''
from pymongo import MongoClient
import os
from dotenv import load_dotenv


username = os.getenv("MONGO_USER")

password = os.getenv("MONGO_PASS")

host = os.getenv("MONGO_HOST")

class DatabaseManager:
    def __init__(self, db_name):
        self.client = MongoClient(f'mongodb://{username}:{password}localhost:27017/')
        self.db = self.client[db_name]

    def query(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)

    def insert(self, collection_name, document):
        collection = self.db[collection_name]
        collection.insert_one(document)
        #result = collection.insert_one(document)
        #return result.inserted_id

    def __del__(self):
        self.client.close()