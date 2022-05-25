from fastapi import APIRouter


router = APIRouter(
    prefix="/home",
    tags=["home"]
)


@router.get("/")
def homepage_endpoint():
    return {"home": "page"}
