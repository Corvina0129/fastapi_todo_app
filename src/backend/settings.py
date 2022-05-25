from pydantic import BaseSettings


class Settings(BaseSettings):
    title: str = "Todo App"
    description: str = "Creating notes about necessary tasks"
    version: str = "1.0.0"

    server_host: str = "127.0.0.1"
    server_port: int = 8080
    database_url: str = "sqlite:///./database.sqlite3"

    jwt_secret: str = "i9-HxQ2RbCGHho1rN1tVhGkPHKXsGCytVXX9_bkgLS4"
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 3600  # in seconds, is 1 hour

    tags_metadata = [
        {
            "name": "home",
            "description": "homepage"
        },
        {
            "name": "auth",
            "description": "registration and authorization"
        },
        {
            "name": "operations",
            "description": "crud operations with todos"
        },

    ]


settings = Settings()
