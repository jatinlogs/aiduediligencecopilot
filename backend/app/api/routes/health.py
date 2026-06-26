from fastapi import APIRouter

from backend.app.config.settings import settings

router = APIRouter()

@router.get("/health", tags =["Health"])
def health_check():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "environment": settings.ENVIRONMENT,
        "version": settings.APP_VERSION,
    }