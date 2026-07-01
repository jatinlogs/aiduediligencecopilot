from pydantic import BaseModel

from backend.app.models.chunk import Chunk


class EmbeddedChunk(BaseModel):
    chunk: Chunk
    embedding: list[float]