import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from . import routers


def create_app() -> FastAPI:
    app = FastAPI(title="Clients App")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3001", "http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    routers.register_routers(app, "app.api.routers.v1", "api")

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logging.error(f"Unexpected error: {str(exc)}. Path: {request.url.path}")
        return JSONResponse(
            status_code=500,
            content={
                "message": "An unexpected error occurred. Please try again later."
            },
        )

    @app.get("/")
    async def root():
        return {"app": "book manager app", "version": "0.1"}

    return app
