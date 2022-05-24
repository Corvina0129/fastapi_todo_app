from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from backend.models.auth import User, Token, UserCreate
from backend.services.auth import fetch_specific_user, AuthService


router = APIRouter(prefix="/auth")


@router.get("/user", response_model=User)
def get_user(user: User = Depends(fetch_specific_user)):
    pass


@router.post("/signup", response_model=Token)
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
    return service.register_new_user(user_data=user_data)


@router.post("/signin", response_model=Token)
def sign_in(
        data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()
):
    pass
