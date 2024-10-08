from pydantic import BaseModel
from datetime import date

class Author(BaseModel):
    id: int
    name: str
    birthdate: date
    nationality: str
