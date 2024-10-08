import json

TEST_JSON_PATH = 'test_data.json'

def test_add_book_append_book_in_json_successfully(
        init_json_book_repository
):
    repository = init_json_book_repository

    new_book_title = "Animal Farm"
    new_author_id = 1
    new_book = repository.add_book(
        book_title=new_book_title,
        author_name="George Orwell",
        published_year=1945,
        total_copies=5,
        author_id=new_author_id
    )

    assert new_book.title == new_book_title
    assert new_book.author_id == new_author_id
    assert new_book.published_year == 1945

    with open(TEST_JSON_PATH, 'r') as f:
        data = json.load(f)

    assert len(data['books']) == 2
    assert data['books'][-1]['title'] == new_book_title
    assert data['books'][-1]['author_id'] == new_author_id

def test_get_book_by_title_and_author_returns_book_when_book_already_exist(
        init_json_book_repository
):
    repository = init_json_book_repository

    book = repository.get_book_by_title_and_author("1984", 1)

    assert book is not None
    assert book.title == "1984"
    assert book.author_id == 1


def test_get_book_by_title_and_author_returns_none_when_no_book_found(
        init_json_book_repository
):
    repository = init_json_book_repository

    book_not_found = repository.get_book_by_title_and_author(
        "Non-existing",
        999
    )

    assert book_not_found is None
