from abc import ABC, abstractmethod
from typing import Optional

from .. import model


class BookRepository(ABC):
    @abstractmethod
    def add_book(
            self,
            book_title: str,
            author_name: str,
            published_year: int,
            total_copies: int,
            author_id: int
    ) -> model.Book:
        pass

    @abstractmethod
    def get_book_by_title_and_author(
            self,
            title: str,
            author_id: int
    ) -> Optional[model.Book]:
        pass
