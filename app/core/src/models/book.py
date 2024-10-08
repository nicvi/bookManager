from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    is_available: bool = True
    borrowed_by: Optional[int] = None
