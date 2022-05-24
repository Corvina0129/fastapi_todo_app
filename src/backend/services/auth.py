from fastapi.security import OAuth2PasswordBearer

oauth = OAuth2PasswordBearer(tokenUrl="/auth/signin/")


def fetch_specific_user():
    pass


class AuthService:
    pass
