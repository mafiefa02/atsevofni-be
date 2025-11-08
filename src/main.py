from fastapi import FastAPI

from src.routers import app_router

app = FastAPI(
    title="Atsevofni Front End Challenge Backend",
    description="Welcome to Atsevofni Front End Challenge's backend documentation!",
    root_path="/api/v1",
)

app.include_router(app_router)
