from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from ..db.tables import User as TableUser
from ..models import auth

from ..db.db import get_session
from ..settings import settings


oauth = OAuth2PasswordBearer(tokenUrl="/auth/signin/")


def fetch_specific_user(token: str = Depends(oauth)) -> auth.User:
    """
    функция связывает токен с фастфпи,
    читает токен из хедера, валидирует его и возвращает клиенту
    """
    return AuthService.validate_token(token)


class AuthService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: auth.UserCreate) -> auth.Token:
        user = TableUser(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password)
        )
        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> auth.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )
        user = (
            self.session
            .query(TableUser)
            .filter(TableUser.username == username)
            .first()
        )
        if not user: raise exception

        if not self.verify_password(
                raw_password=password,
                hashed_password=user.password_hash
        ):
            raise exception

        return self.create_token(user)

    @classmethod
    def verify_password(cls, raw_password: str, hashed_password: str) -> bool:
        """

        :param raw_password: сырой пароль в откытом виде из формы авторизации
        :param hashed_password: хэш из бд
        :return: либо хэш совпадает, либо нет
        """
        return bcrypt.verify(raw_password, hashed_password)

    @classmethod
    def hash_password(cls, raw_password: str) -> str:
        return bcrypt.hash(raw_password)

    @classmethod
    def create_token(cls, user: TableUser) -> auth.Token:
        user_data = auth.User.from_orm(user)
        utctime = datetime.utcnow()

        payload = {
            "iat": utctime,
            "nbf": utctime,
            "exp": utctime + timedelta(seconds=settings.jwt_expiration),
            "sub": str(user_data.id),
            "user": user_data.dict()
        }

        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm
        )

        return auth.Token(access_token=token)

    @classmethod
    def validate_token(cls, token: str):
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            raise exception from None

        user_data = payload.get("user")

        try:
            user = auth.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user
