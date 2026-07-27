from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.mongo import init_mongo, close_mongo
from app.db.chroma import init_chroma, close_chroma

# 1. Define the Lifespan Context Manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP ---
    print("🚀 Starting up LexiRAG application...")
    init_mongo()
    init_chroma()
    
    yield  # This is where the app runs and handles requests
    
    # --- SHUTDOWN ---
    print("🛑 Shutting down LexiRAG application...")
    close_mongo()
    close_chroma()

# 2. Initialize FastAPI App
app = FastAPI(
    title="LexiRAG API",
    description="Legal Contract & Case Law Analyzer",
    version="1.0.0",
    lifespan=lifespan
)

# 3. Basic Health Check Route
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy", 
        "message": "LexiRAG API is running and ready for legal analysis!"
    }

# Note: We will include our routers (chat.py, documents.py) here in later phases.
# from app.api import chat, documents
# app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
# app.include_router(documents.router, prefix="/api/v1/documents", tags=["Documents"])