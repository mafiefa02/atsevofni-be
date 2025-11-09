from fastapi import FastAPI

from .configs import settings
from .routers import app_router

app = FastAPI(
    title=f"{settings.app_name}'s Documentation",
    description=f"Welcome to {settings.app_name}'s documentation page!",
    root_path="/api/v1",
)

app.include_router(app_router)
