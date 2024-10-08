from .. import repositories, model, exceptions


class AddBook:
    def __init__(
            self,
            book_repository: repositories.BookRepository,
            author_repository: repositories.AuthorRepository
    ):
        self.book_repository = book_repository
        self.author_repository = author_repository

    def execute(
            self,
            book_title: str,
            author_name: str,
            published_year: int,
            total_copies: int
    ) -> model.Book:
        author = self.author_repository.get_author_by_name(author_name)
        if not author:
            raise exceptions.AuthorNotFound(author = author_name)

        existing_book = self.book_repository.get_book_by_title_and_author(
            title= book_title, author_id= author.id
        )
        if existing_book:
            raise exceptions.BookAlreadyExists(book_title, author_name)

        added_book = self.book_repository.add_book(
            book_title=book_title,
            author_name=author_name,
            published_year=published_year,
            total_copies=total_copies,
            author_id=author.id
        )
        return added_book
