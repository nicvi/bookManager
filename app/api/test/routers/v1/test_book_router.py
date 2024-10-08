import pytest

from app import core
from app.api import dependencies
from app.main import app


@pytest.mark.asyncio
async def test_add_book_return_success(client_api, mock_add_book_use_case):
    app.dependency_overrides[dependencies.add_book_use_case] = \
        lambda: mock_add_book_use_case
    expected_response = {
        "id" : 1,
        "title" : "Test Book",
        "author_id" : 1,
        "published_year" : 2023,
        "is_borrowed" : False,
        "borrowers" : [],
        "available_copies" : 5,
        "total_copies" : 10,
    }

    response = await client_api.post("/api/book", json={
        "book_title": "Test Book",
        "author_name": "Test Author",
        "published_year": 2023,
        "total_copies": 10
    })

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_add_book_capture_exception_when_author_not_found(
        client_api, mock_add_book_use_case
):
    mock_add_book_use_case.execute.side_effect = \
        core.exceptions.AuthorNotFound(author="Unknown Author")
    app.dependency_overrides[dependencies.add_book_use_case] = \
        lambda: mock_add_book_use_case

    response = await client_api.post("/api/book", json={
        "book_title": "Test Book",
        "author_name": "Unknown Author",
        "published_year": 2023,
        "total_copies": 10
    })

    assert response.status_code == 404
    assert response.json() == {"detail": "Author, Unknown Author, not found."}
    del app.dependency_overrides[dependencies.add_book_use_case]


@pytest.mark.asyncio
async def test_add_book_capture_exception_when_book_already_exists(
        client_api, mock_add_book_use_case
):
    mock_add_book_use_case.execute.side_effect = \
        core.exceptions.BookAlreadyExists(
            book_title="Test Book",
            author_name="Test Author"
        )
    app.dependency_overrides[dependencies.add_book_use_case] = \
        lambda: mock_add_book_use_case

    response = await client_api.post("/api/book", json={
        "book_title": "Test Book",
        "author_name": "Test Author",
        "published_year": 2023,
        "total_copies": 10
    })

    assert response.status_code == 400
    assert response.json() == {
        "detail": "The book 'Test Book' by author 'Test Author' already exists."
    }
    del app.dependency_overrides[dependencies.add_book_use_case]

@pytest.mark.asyncio
async def test_add_book_capture_exception_when_internal_server_error_happens(
        client_api, mock_add_book_use_case
):
    mock_add_book_use_case.execute.side_effect = Exception("Unexpected error")
    app.dependency_overrides[dependencies.add_book_use_case] = \
        lambda: mock_add_book_use_case

    response = await client_api.post("/api/book", json={
        "book_title": "Test Book",
        "author_name": "Test Author",
        "published_year": 2023,
        "total_copies": 10
    })

    assert response.status_code == 500
    assert response.json() == {"detail": "Unexpected error"}
    del app.dependency_overrides[dependencies.add_book_use_case]
