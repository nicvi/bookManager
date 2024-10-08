import json
from typing import Optional

from app import core


class JsonBookRepository(core.BookRepository):
    def __init__(self, json_file_path: str):
        self.books = None
        self.json_file_path = json_file_path
        self.load_books()

    def load_books(self):
        with open(self.json_file_path, 'r') as f:
            data = json.load(f)
            self.books = [core.Book(**book) for book in data['books']]

    def save_books(self, new_book: core.Book):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)

        data['books'].append(new_book.dict())

        with open(self.json_file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_book(
            self,
            book_title: str,
            author_name: str,
            published_year: int,
            total_copies: int,
            author_id: int,
    ) -> core.Book:
        new_book = core.Book(
            id=len(self.books) + 1,
            title=book_title,
            author_id=author_id,
            published_year=published_year,
            is_borrowed=False,
            borrowers=[],
            available_copies=total_copies,
            total_copies=total_copies
        )
        self.books.append(new_book)
        self.save_books(new_book)
        return new_book

    def get_book_by_title_and_author(
            self,
            title: str,
            author_id: int
    ) -> Optional[core.Book]:
        for book in self.books:
            if book.title == title and book.author_id == author_id:
                return book
        return None
