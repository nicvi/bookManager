import json
from typing import Optional

from app import core


class JsonAuthRepository(core.AuthorRepository):
    def __init__(self, json_file_path: str):
        self.authors = None
        self.json_file_path = json_file_path
        self.load_authors()

    def load_authors(self):
        with open(self.json_file_path, 'r') as f:
            data = json.load(f)
            self.authors = [core.model.Author(**author) for author in data['authors']]

    def get_author_by_name(self, name: str) -> Optional[core.model.Author]:
        for author in self.authors:
            if author.name.lower() == name.lower():
                return author
        return None

