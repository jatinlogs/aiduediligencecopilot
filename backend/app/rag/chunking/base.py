from abc import ABC, abstractmethod

from backend.app.models.document import Document
from backend.app.models.chunk import Chunk


class ChunkingStrategy(ABC):

    @abstractmethod
    def chunk_documents(
        self,
        documents: list[Document],
    ) -> list[Chunk]:
        """
        Convert documents into chunks.
        """
        pass