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
    ) -> model.Book:
        pass

    @abstractmethod
    def get_book_by_title_and_author(
            self,
            title: str,
            author: int
    ) -> Optional[model.Book]:
        pass

    @abstractmethod
    def get_books(self) -> list[model.Book]:
        pass

    @abstractmethod
    def get_book_by_id(self, book_id: int) -> model.Book:
        pass

    @abstractmethod
    def get_books_by_author(self, author_id: model.Book) -> list[model.Book]:
        pass

    @abstractmethod
    def check_book_status(self, book_id: int):
        pass
