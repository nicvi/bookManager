import inspect
from importlib import import_module
from typing import Optional

from fastapi import FastAPI

from .. import config


def register_routers(
    app: FastAPI, routers_path: str, stg_name: Optional[str] = ""
) -> None:
    router_module = import_module(routers_path)
    routers = inspect.getmembers(
        router_module, lambda member: isinstance(member, config.APIRouter)
    )
    for name, router in routers:
        prefix = "" if name == "index" else f'/{name.replace("_", "-")}'
        app.include_router(
            router, tags=[name], prefix=f"/{stg_name}{prefix}" if stg_name else prefix
        )
