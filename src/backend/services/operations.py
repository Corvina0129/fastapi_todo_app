from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import tables
from ..db.db import get_session
from ..models.operations import (
    TodoOperationCreate,
    TodoOperationUpdate,
)


class OperationService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_todo(self, user_id: int, todo_id: int) -> tables.Todo:
        todo = (
            self.session
            .query(tables.Todo)
            .filter_by(id=todo_id, user_id=user_id)
            .first()
        )
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return todo

    def get_todos_list(self, user_id: int) -> list[tables.Todo]:
        query = (
            self.session
            .query(tables.Todo)
            .filter_by(user_id=user_id)
        )
        todos = query.all()

        return todos

    def get_specific_todo(self, user_id: int, todo_id: int) -> tables.Todo:
        return self._get_todo(user_id=user_id ,todo_id=todo_id)

    def create_todo(self,user_id: int, operation: TodoOperationCreate) -> tables.Todo:
        todo = tables.Todo(
            **operation.dict(),
            user_id=user_id
        )
        self.session.add(todo)
        self.session.commit()

        return todo

    def update_todo(
            self,
            user_id: int,
            todo_id: int,
            operation: TodoOperationUpdate
    ) -> tables.Todo:

        todo = self._get_todo(user_id=user_id, todo_id=todo_id)
        for field, value in operation:
            setattr(todo, field, value)
        self.session.commit()

        return todo

    def delete_todo(self,user_id: int, todo_id: int):
        todo = self._get_todo(user_id=user_id, todo_id=todo_id)
        self.session.delete(todo)
        self.session.commit()
