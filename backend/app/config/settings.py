from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str
    DEBUG: bool

    # LLM
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str

    # Embeddings
    EMBEDDING_MODEL: str
    RERANKER_MODEL: str

    # Qdrant
    QDRANT_URL: str
    QDRANT_COLLECTION: str

    # Neo4j
    NEO4J_URI: str = ""
    NEO4J_USERNAME: str = ""
    NEO4J_PASSWORD: str = ""

    # Retrieval
    TOP_K: int
    FINAL_TOP_K: int
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache # helps in not need to load again and again the settings from env file
def get_settings() -> Settings:
    return Settings()


settings = get_settings()