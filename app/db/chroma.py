import chromadb
from app.core.config import settings

class ChromaDB:
    client: chromadb.ClientAPI = None
    collection: chromadb.Collection = None

# Singleton pattern to ensure only one instance of ChromaDB is created
chromadb_instance = ChromaDB()

def init_chromaDB():
    """ Initialize chromadb connection"""
     # Using HttpClient to connect to a standalone Chroma server (Best practice for production)
    chromadb_instance.client = chromadb.HttpClient(
        host=settings.chroma_host,
        port=settings.chroma_port
    )
    # Get or create the collection
    # We use cosine similarity, which is standard for text embeddings
    chromadb_instance.collection = chromadb_instance.client.get_or_create_collection(
        name=settings.chroma_collection,
        metadata={"hnsw:space": "cosine"}
    )
    print("ChromaDB connection established successfully.")

def close_chromaDB():
    """ Reset ChromaDB instance"""
    chromadb_instance.client = None
    chromadb_instance.collection = None
    print("ChromaDB connection closed.")