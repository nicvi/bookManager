import pytest
from fastapi import FastAPI

from app.api import config


@pytest.mark.asyncio
async def test_custom_api_router_routes(custom_client_api):
    app = FastAPI()
    router = config.APIRouter()

    @router.get("/test/")
    def test_endpoint():
        return {"message": "success"}

    app.include_router(router)
    mock_client_api = custom_client_api(app)

    response = await mock_client_api.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "success"}

    response = await mock_client_api.get("/test/")
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
