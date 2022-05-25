from fastapi import FastAPI

from .api import router as main_api_router
from .settings import settings


app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    openapi_tags=settings.tags_metadata
)

app.include_router(main_api_router)
