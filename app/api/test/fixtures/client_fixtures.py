import httpx
import pytest

from app import app


@pytest.fixture
def client_api():
    transport = httpx.ASGITransport(app=app)
    return httpx.AsyncClient(transport=transport, base_url="http://test")


@pytest.fixture
def custom_client_api():
    def _create_fixture(custom_app=app):
        transport = httpx.ASGITransport(app=custom_app)
        return httpx.AsyncClient(transport=transport, base_url="http://test")

    return _create_fixture
