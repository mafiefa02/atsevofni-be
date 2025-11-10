from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .configs import settings
from .routers import app_router

app = FastAPI(
    title=f"{settings.app_name}'s Documentation",
    description=f"Welcome to {settings.app_name}'s documentation page!",
    root_path="/api/v1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router)
