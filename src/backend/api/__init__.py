from fastapi import APIRouter

from . import home
from . import operations
from . import auth


router = APIRouter()
router.include_router(home.router)
router.include_router(auth.router)
router.include_router(operations.router)
