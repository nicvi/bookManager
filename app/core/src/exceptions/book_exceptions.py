class BookAlreadyExists(Exception):

    def __init__(self, book_title: str, author_name: str) -> None:
        self.book_title = book_title
        self.author_name= author_name
        super().__init__(
            f"The book '{book_title}' by author '{author_name}' already exists."
        )
