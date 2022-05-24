from datetime import date
from pydantic import BaseModel


class BaseTodoOperation(BaseModel):
    date: date
    todo_name: str
    description: str
    is_completed: bool


class TodoOperation(BaseTodoOperation):
    id: int

    class Config:
        orm_mode = True


class TodoOperationCreate(BaseTodoOperation):
    pass


class TodoOperationUpdate(BaseTodoOperation):
    pass


class TodoOperationDelete(BaseTodoOperation):
    pass
