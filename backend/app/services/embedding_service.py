from backend.app.config.settings import settings
from backend.app.rag.embeddings.bge import BGEEmbeddingModel


from backend.app.models.chunk import Chunk
from backend.app.models.embedding import EmbeddedChunk


class EmbeddingService:

    def __init__(self):

        self.embedding_model = BGEEmbeddingModel(
            settings.EMBEDDING_MODEL
        )

    def embed_chunk(
        self,
        chunk: Chunk,
    ) -> EmbeddedChunk:

        vector = self.embedding_model.embed_document(
            chunk.text
        )

        return EmbeddedChunk(
            chunk=chunk,
            embedding=vector,
        )

    def embed_chunks(
        self,
        chunks: list[Chunk],
    ) -> list[EmbeddedChunk]:

        texts = [
            chunk.text
            for chunk in chunks
        ]

        vectors = self.embedding_model.embed_documents(
            texts
        )

        embedded_chunks = []

        for chunk, vector in zip(chunks, vectors):

            embedded_chunks.append(

                EmbeddedChunk(
                    chunk=chunk,
                    embedding=vector,
                )

            )

        return embedded_chunks

    def embed_query(
        self,
        query: str,
    ) -> list[float]:

        return self.embedding_model.embed_query(
            query
        )