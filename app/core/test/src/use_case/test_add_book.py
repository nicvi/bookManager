import pytest
from unittest.mock import MagicMock

from app.core.src import model, exceptions


def test_add_book_returns_success(
        add_book_service, book_repository, author_repository
):
    mock_author = MagicMock(id=1, name="John Doe")
    author_repository.get_author_by_name.return_value = mock_author
    book_repository.get_book_by_title_and_author.return_value = None
    mock_added_book = model.Book(
        id=1,
        title="Sample Book",
        author_id=1,
        published_year=2020,
        is_borrowed= False,
        borrowers= [],
        available_copies= 2,
        total_copies=10,
    )
    book_repository.add_book.return_value = mock_added_book

    result = add_book_service.execute(
        book_title="Sample Book",
        author_name="John Doe",
        published_year=2020,
        total_copies=10
    )

    assert result == mock_added_book
    author_repository.get_author_by_name.assert_called_once_with("John Doe")
    book_repository.get_book_by_title_and_author.assert_called_once_with(
        title="Sample Book", author=mock_author.id)
    book_repository.add_book.assert_called_once_with(
        "Sample Book", "John Doe", 2020, 10)


def test_add_book_raise_exception_when_author_not_found(
        add_book_service, book_repository, author_repository
):
    author_repository.get_author_by_name.return_value = None

    with pytest.raises(exceptions.AuthorNotFound) as exception_params:
        add_book_service.execute(
            book_title="Sample Book",
            author_name="Unknown Author",
            published_year=2020,
            total_copies=10
        )

    assert exception_params.value.author == "Unknown Author"
    author_repository.get_author_by_name.assert_called_once_with("Unknown Author")
    book_repository.get_book_by_title_and_author.assert_not_called()
    book_repository.add_book.assert_not_called()


def test_add_book_raise_exception_when_book_already_exists(
        add_book_service, book_repository, author_repository
):
    mock_author = MagicMock(id=1, name="John Doe")
    author_repository.get_author_by_name.return_value = mock_author

    mock_existing_book = MagicMock(id=1, title="Sample Book", author_id=1)
    book_repository.get_book_by_title_and_author.return_value = mock_existing_book

    with pytest.raises(exceptions.BookAlreadyExists) as exception_params:
        add_book_service.execute(
            book_title="Sample Book",
            author_name="John Doe",
            published_year=2020,
            total_copies=10
        )

    assert exception_params.value.book_title == "Sample Book"
    assert exception_params.value.author_name == "John Doe"
    author_repository.get_author_by_name.assert_called_once_with("John Doe")
    book_repository.get_book_by_title_and_author.assert_called_once_with(
        title="Sample Book", author=mock_author.id
    )
    book_repository.add_book.assert_not_called()
