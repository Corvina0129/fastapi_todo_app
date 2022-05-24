from fastapi import APIRouter, Depends, Response, status

from backend.models.auth import User
from src.backend.models.operations import (
    TodoOperation,
    TodoOperationCreate,
    TodoOperationUpdate
)
from src.backend.services.operations import OperationService


router = APIRouter(prefix="/operations")


@router.get("/", response_model=list[TodoOperation])
def get_all_user_todos(
        # user: User = Depends(get_user),
        service: OperationService = Depends()
):
    return service.get_todos_list()


@router.get("/{todo_id}", response_model=TodoOperation)
def get_specific_todo(
        todo_id: int,
        service: OperationService = Depends()
):
    return service.get_specific_todo(todo_id=todo_id)


@router.post("/", response_model=TodoOperation)
def create_todo(
        operation_data: TodoOperationCreate,
        service: OperationService = Depends()
):
    return service.create_todo(operation=operation_data)


@router.put("/{todo_id}", response_model=TodoOperation)
def update_todo(
        todo_id: int,
        operation_data: TodoOperationUpdate,
        service: OperationService = Depends()
):
    return service.update_todo(
        todo_id=todo_id,
        operation=operation_data
    )


@router.delete("/{todo_id}")
def delete_todo(
        todo_id: int,
        service: OperationService = Depends()
):
    service.delete_todo(todo_id=todo_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

