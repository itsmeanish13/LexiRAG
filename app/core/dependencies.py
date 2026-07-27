from pymongo.database import Database
from chromadb import Collection
from app.db.mongo import mongodb
from app.db.chroma import chromadb_instance

def get_mongo_db() -> Database:
    """Get the MongoDB database instance."""
    return mongodb.db

def get_chroma_collection() -> Collection:
    """Get the ChromaDB collection instance."""
    return chromadb_instance.collection