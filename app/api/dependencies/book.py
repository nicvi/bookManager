from app import core
from app.adapters import repositories
from app import factories

def add_book_use_case() -> core.AddBook:
    json_data_source = factories.settings.JSON_DATA_SOURCE
    book_repository = repositories.JsonBookRepository(json_data_source)
    author_repository = repositories.JsonAuthRepository(json_data_source)
    return core.AddBook(
        book_repository=book_repository,
        author_repository=author_repository
    )
