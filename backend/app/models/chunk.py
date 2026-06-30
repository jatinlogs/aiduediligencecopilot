from pydantic import BaseModel


class Chunk(BaseModel):
    chunk_id: str

    company: str
    year: int
    source: str
    page: int
    text: str