from pydantic import BaseModel
from typing import List

class Borrower(BaseModel):
    user_id: int
    borrow_date: str

class Book(BaseModel):
    id: int
    title: str
    author_id: int
    published_year: int
    is_borrowed: bool
    borrowers: List[Borrower]
    available_copies: int
    total_copies: int
