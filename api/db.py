'''
Name: db.py
Description: Database connection manager for
'''
from pymongo import MongoClient
import os
from dotenv import load_dotenv


user = os.getenv("MONGO_USER")

pwd = os.getenv("MONGO_PASS")

host = os.getenv("MONGO_HOST")

connection = f"mongodb://{user}:{pwd}@{host}/"
class DatabaseManager:
    def __init__(self, db_name):
        self.client = MongoClient(connection)
        self.db = self.client[db_name]

    def query(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)

    def insert(self, collection_name, document):
        collection = self.db[collection_name]
        collection.insert_one(document)
        #result = collection.insert_one(document)
        #return result.inserted_id

