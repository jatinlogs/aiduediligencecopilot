from qdrant_client.models import Distance
from qdrant_client.models import VectorParams

from backend.app.database.qdrant_client import QdrantVectorDatabase
from backend.app.config.settings import settings

# moved this to qdrant_client.py to avoid circular import issues
class VectorStore:

    def __init__(self):

        self.db = QdrantVectorDatabase()

        self.client = self.db.client

    def create_collection(self):

        collections = self.client.get_collections()

        existing = [
            collection.name
            for collection in collections.collections
        ]

        if settings.QDRANT_COLLECTION in existing:

            print("Collection already exists.")

            return

        self.client.create_collection(

            collection_name=settings.QDRANT_COLLECTION,

            vectors_config=VectorParams(

                size=settings.VECTOR_SIZE,

                distance=Distance.COSINE,

            ),

        )

        print("Collection created.")