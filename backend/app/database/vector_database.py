from abc import ABC, abstractmethod

from backend.app.models.embedding import EmbeddedChunk


class VectorDatabase(ABC):

    @abstractmethod
    def create_collection(self):
        pass

    @abstractmethod
    def upload(self, chunks: list[EmbeddedChunk]):
        pass

    @abstractmethod
    def search(
        self,
        vector: list[float],
        limit: int,
    ):
        pass

    @abstractmethod
    def delete_collection(self):
        pass