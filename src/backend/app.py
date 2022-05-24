from fastapi import FastAPI

from .api import router as main_api_router

app = FastAPI()
app.include_router(main_api_router)
