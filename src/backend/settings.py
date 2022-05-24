from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My Todo App"
    server_host: str = "127.0.0.1"
    server_port: int = 8080
    database_url: str = "sqlite:///./database.sqlite3"

    #auth
    jwt_secret: str = "i9-HxQ2RbCGHho1rN1tVhGkPHKXsGCytVXX9_bkgLS4"
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 3600  # in seconds, is 1 hour


settings = Settings()
