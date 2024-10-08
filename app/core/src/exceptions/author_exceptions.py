class AuthorNotFound(Exception):

    def __init__(self, author: str) -> None:
        self.author = author
        super().__init__(f"Author, {author}, not found.")
