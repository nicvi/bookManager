from pydantic import BaseModel


class BookCreateDTO(BaseModel):
    book_title: str
    author_name: str
    published_year: int
    total_copies: int
