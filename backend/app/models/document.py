from pydantic import BaseModel

class Document(BaseModel):
    company:str
    year:int
    source:str
    page:int
    text:str