from pymongo import MongoClient
from pymongo.database import Database
from app.core.config import settings

class MongoDB:
    client: MongoClient = None
    db: Database = None

# Singleton pattern to ensure only one instance of MongoDB is created
mongodb = MongoDB()

def init_mongoDB():
    """ Initialize the MongoDB client and database connection. """
    mongodb.client = MongoClient(settings.mongo_uri)
    mongodb.db = mongodb.client[settings.mongo_db_name]
    print("MongoDB connection established successfully.")

def close_mongo():
    """ Close the MongoDB client connection. """
    if mongodb.client:
        mongodb.client.close()
        print("MongoDB connection closed.")