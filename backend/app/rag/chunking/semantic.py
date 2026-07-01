from backend.app.rag.chunking.base import ChunkingStrategy


class SemanticChunker(ChunkingStrategy):

    def chunk_documents(self, documents):
        raise NotImplementedError(
            "Semantic chunking will be implemented later."
        )