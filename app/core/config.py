from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    #Groq Settings
    groq_api_key:str
    groq_model:str = "llama3-70b-8192"

    #MongoDB Settings
    mongo_uri: str = "mongodb://localhost:27017"
    mongo_db_name: str = "lexirag_db"

    #ChromaDB Settings
    chroma_host: str = "localhost"
    chroma_port: int = 8000
    chroma_collection: str = "legal_vectors"

    #App Settings
    app_env: str = "development"

    #pydantic config to load .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

#Instantiate the settings object
settings = Settings()