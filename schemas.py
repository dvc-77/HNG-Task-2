from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str

class ResponsePersonBase(BaseModel):
    name: str
    id: int