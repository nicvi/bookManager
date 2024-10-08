from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI

from ... import config, routers


@pytest.mark.asyncio
async def test_register_routers_with_prefix(custom_client_api):
    app = FastAPI()

    mock_router1 = config.APIRouter()

    @mock_router1.get("/test1")
    def test1():
        return {"message": "test1"}

    mock_router2 = config.APIRouter()

    @mock_router2.get("/test2")
    def test2():
        return {"message": "test2"}

    mock_module = MagicMock()
    mock_module.index = mock_router1
    mock_module.other_router = mock_router2
    with patch("app.api.routers.register.import_module", return_value=mock_module):
        routers.register_routers(app, "mock_routers_path", stg_name="v1")

    mock_client_api = custom_client_api(app)

    response = await mock_client_api.get("/v1/test1")
    assert response.status_code == 200
    assert response.json() == {"message": "test1"}

    response = await mock_client_api.get("/v1/other-router/test2")
    assert response.status_code == 200
    assert response.json() == {"message": "test2"}


@pytest.mark.asyncio
async def test_register_routers_without_stg_name(custom_client_api):
    app = FastAPI()

    mock_router1 = config.APIRouter()

    @mock_router1.get("/route")
    def index():
        return {"message": "index"}

    mock_router2 = config.APIRouter()

    @mock_router2.get("/")
    def other():
        return {"message": "other"}

    mock_module = MagicMock()
    mock_module.index = mock_router1
    mock_module.other_router = mock_router2
    with patch("app.api.routers.register.import_module", return_value=mock_module):
        routers.register_routers(app, "mock_routers_path")

    mock_client_api = custom_client_api(app)

    response = await mock_client_api.get("/route")
    assert response.status_code == 200
    assert response.json() == {"message": "index"}

    response = await mock_client_api.get("/other-router/")
    assert response.status_code == 200
    assert response.json() == {"message": "other"}
