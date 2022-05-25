import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String, unique=True)
    username = sa.Column(sa.String, unique=True)
    password_hash = sa.Column(sa.String)


class Todo(Base):
    __tablename__ = "todos"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), index=True)
    date = sa.Column(sa.Date)
    todo_name = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)
    is_completed = sa.Column(sa.Boolean, default=False)
