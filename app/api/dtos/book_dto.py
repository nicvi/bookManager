from typing import List
from pydantic import BaseModel

class CreateBookRequestDTO(BaseModel):
    book_title: str
    author_name: str
    published_year: int
    total_copies: int

class BorrowerDTO(BaseModel):
    user_id: int
    borrow_date: str

class BookResponseDTO(BaseModel):
    id: int
    title: str
    author_id: int
    published_year: int
    is_borrowed: bool
    borrowers: List[BorrowerDTO] = []
    available_copies: int
    total_copies: int

    class Config:
        orm_mode = True
