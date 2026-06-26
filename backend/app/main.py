from fastapi import FastAPI

from backend.app.api.router import api_router
from backend.app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(
    api_router,
    prefix="/api/v1",
)