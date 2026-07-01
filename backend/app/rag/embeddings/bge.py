from sentence_transformers import SentenceTransformer

from backend.app.rag.embeddings.base import BaseEmbeddingModel



class BGEEmbeddingModel(BaseEmbeddingModel):

    QUERY_PREFIX = (
        "Represent this sentence for searching relevant passages: "
    )

    def __init__(self, model_name: str):

        self.model = SentenceTransformer(model_name)

    def embed_document(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            normalize_embeddings=True,
        )

        return embeddings.tolist()

    def embed_query(
        self,
        query: str,
    ) -> list[float]:

        query = self.QUERY_PREFIX + query

        embedding = self.model.encode(
            query,
            normalize_embeddings=True,
        )

        return embedding.tolist()