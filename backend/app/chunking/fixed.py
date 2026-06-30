import uuid

from backend.app.config.settings import settings
from backend.app.models.chunk import Chunk
from backend.app.models.document import Document
from backend.app.chunking.base import ChunkingStrategy



class FixedCharacterChunker(ChunkingStrategy):
    def __init__(self,chunk_size: int = settings.CHUNK_SIZE,chunk_overlap: int = settings.CHUNK_OVERLAP):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_documents(self, documents: list[Document]) -> list[Chunk]:

        chunks = []

        for document in documents:

            text = document.text

            start = 0

            while start < len(text):

                end = start + self.chunk_size

                chunk_text = text[start:end]

                chunk = Chunk(
                    chunk_id=str(uuid.uuid4()),
                    company=document.company,
                    year=document.year,
                    source=document.source,
                    page=document.page,
                    text=chunk_text,
                )

                chunks.append(chunk)

                start += self.chunk_size - self.chunk_overlap # we overlap with 200 words in order to maintain the context of the text, as it cuts down from a single point

        return chunks