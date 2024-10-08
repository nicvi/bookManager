from unittest.mock import MagicMock

import pytest

from app.core.src import repositories, use_cases


@pytest.fixture
def book_repository():
    return MagicMock(spec=repositories.BookRepository)


@pytest.fixture
def author_repository():
    return MagicMock(spec=repositories.AuthorRepository)


@pytest.fixture
def add_book_service(book_repository, author_repository):
    return use_cases.AddBook(
        book_repository=book_repository, author_repository=author_repository
    )
