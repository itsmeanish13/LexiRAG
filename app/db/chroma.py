import chromadb
from pathlib import Path
from app.core.config import settings

class ChromaDB:
    client: chromadb.ClientAPI = None
    collection: chromadb.Collection = None

# Singleton instance
chromadb_instance = ChromaDB()

def init_chroma():
    """Initialize ChromaDB connection using a local persistent client."""
    # 1. Create a local directory for Chroma data if it doesn't exist
    chroma_dir = Path("./chroma_data")
    chroma_dir.mkdir(exist_ok=True)
    
    # 2. Use PersistentClient (No separate server needed, perfect for local dev)
    chromadb_instance.client = chromadb.PersistentClient(path=str(chroma_dir))
    
    # 3. Get or create the collection
    chromadb_instance.collection = chromadb_instance.client.get_or_create_collection(
        name=settings.chroma_collection,
        metadata={"hnsw:space": "cosine"} # Cosine similarity is standard for text
    )
    print("✅ ChromaDB Connected (Local Persistent Mode)")

def close_chroma():
    """Reset ChromaDB instance."""
    chromadb_instance.client = None
    chromadb_instance.collection = None
    print("🔌 ChromaDB Disconnected")