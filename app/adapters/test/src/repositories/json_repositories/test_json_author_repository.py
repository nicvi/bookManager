def test_get_author_by_name_return_author_when_exist(
        init_json_author_repository
):
    repository = init_json_author_repository

    author = repository.get_author_by_name("George Orwell")

    assert author is not None
    assert author.id == 1
    assert author.name == "George Orwell"

def test_get_author_returns_none_when_author_not_found(
        init_json_author_repository
):
    repository = init_json_author_repository

    author = repository.get_author_by_name("Non-existing Author")

    assert author is None

def test_get_author_is_not_case_insensitive_when_search_author(
        init_json_author_repository
):
    repository = init_json_author_repository

    author = repository.get_author_by_name("george orwell")

    assert author is not None
    assert author.id == 1
    assert author.name == "George Orwell"

def test_get_author_return_author_with_different_case(
        init_json_author_repository
):
    repository = init_json_author_repository

    author = repository.get_author_by_name("J.K. ROWLING")

    assert author is not None
    assert author.id == 2
    assert author.name == "J.K. Rowling"
