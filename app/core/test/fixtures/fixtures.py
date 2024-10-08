from unittest.mock import MagicMock

import pytest

from app.core.src import repositories, use_cases, model


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

@pytest.fixture
def mocked_book():
    mock_book = model.Book(
        id=1,
        title="Test Book",
        author_id=1,
        published_year=2023,
        is_borrowed=False,
        borrowers=[],
        available_copies=5,
        total_copies=10,
    )
    return mock_book

@pytest.fixture
def mock_add_book_use_case(mocked_book):
    mock_use_case = MagicMock()
    mock_use_case.execute.return_value = mocked_book
    return mock_use_case
