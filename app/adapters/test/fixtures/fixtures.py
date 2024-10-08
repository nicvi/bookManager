import json
import os
import pytest

from app.adapters import repositories

TEST_JSON_PATH = 'test_data.json'
INITIAL_DATA = {
    "books": [
        {
            "id": 1,
            "title": "1984",
            "author_id": 1,
            "published_year": 1949,
            "is_borrowed": False,
            "borrowers": [],
            "available_copies": 5,
            "total_copies": 5
        }
    ],
    "authors": [
        {
            "id": 1,
            "name": "George Orwell",
            "birthdate": "1903-06-25",
            "nationality": "British"
        },
        {
            "id": 2,
            "name": "J.K. Rowling",
            "birthdate": "1965-07-31",
            "nationality": "British"
        }
    ]
}


@pytest.fixture(scope='module')
def setup_test_json():
    with open(TEST_JSON_PATH, 'w') as file:
        json.dump(INITIAL_DATA, file, indent=4)

    yield

    if os.path.exists(TEST_JSON_PATH):
        os.remove(TEST_JSON_PATH)

@pytest.fixture
def init_json_author_repository(setup_test_json):
    return repositories.JsonAuthRepository(TEST_JSON_PATH)

@pytest.fixture
def init_json_book_repository(setup_test_json):
    return repositories.JsonBookRepository(TEST_JSON_PATH)