import json
import os
import pytest
from unittest.mock import patch

from app import core
from app.adapters import repositories
from app.api import dependencies


TEST_JSON_PATH = 'test_data.json'

def test_add_book_use_case_dependency_returns_correct_use_case(setup_test_json):
    with patch('app.factories.settings.JSON_DATA_SOURCE', TEST_JSON_PATH):
        use_case = dependencies.add_book_use_case()

        assert isinstance(use_case, core.AddBook)
        assert isinstance(use_case.book_repository, repositories.JsonBookRepository)
        assert isinstance(use_case.author_repository, repositories.JsonAuthRepository)

        assert use_case.book_repository.json_file_path == TEST_JSON_PATH
        assert use_case.author_repository.json_file_path == TEST_JSON_PATH
