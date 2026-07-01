from qdrant_client import QdrantClient

from backend.app.config.settings import settings
from backend.app.database.vector_database import VectorDatabase

from qdrant_client.models import PointStruct

from backend.app.models.embedding import EmbeddedChunk

from qdrant_client.models import Distance,VectorParams

# inheriting vector database to implement qdrant specific methods
class QdrantVectorDatabase(VectorDatabase):

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL
        )
    
    def upload(
        self,
        chunks: list[EmbeddedChunk],
    ):

        points = []

        for chunk in chunks:

            points.append(

                PointStruct(

                    id=chunk.chunk.chunk_id,

                    vector=chunk.embedding,

                    payload={

                        "company": chunk.chunk.company,

                        "year": chunk.chunk.year,

                        "page": chunk.chunk.page,

                        "source": chunk.chunk.source,

                        "text": chunk.chunk.text,

                    },

                )

            )

        self.client.upsert(

            collection_name=settings.QDRANT_COLLECTION,

            wait=True,

            points=points,

        )

    def search(
        self,
        vector: list[float],
        limit: int = 5,
    ):

        return self.client.query_points(

            collection_name=settings.QDRANT_COLLECTION,

            query=vector,

            limit=limit,

            with_payload=True,

        )
    
    def create_collection(self):

        collections = self.client.get_collections()

        existing = [
            c.name
            for c in collections.collections
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

    def delete_collection(self, collection_name: str):
        raise NotImplementedError
