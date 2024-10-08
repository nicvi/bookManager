from abc import ABC, abstractmethod
from typing import Optional

from .. import model

class AuthorRepository(ABC):
    @abstractmethod
    def get_author_by_name(self, name: str) -> Optional[model.Author]:
        pass
