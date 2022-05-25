from fastapi import APIRouter, Depends, Response, status

from ..models.auth import User
from ..models.operations import (
    TodoOperation,
    TodoOperationCreate,
    TodoOperationUpdate
)
from ..services.auth import fetch_specific_user
from ..services.operations import OperationService


router = APIRouter(
    prefix="/operations",
    tags=["operations"]
)


@router.get("/", response_model=list[TodoOperation])
def get_all_user_todos(
        user: User = Depends(fetch_specific_user),
        service: OperationService = Depends()
):
    return service.get_todos_list(user_id=user.id)


@router.get("/{todo_id}", response_model=TodoOperation)
def get_specific_todo(
        todo_id: int,
        user: User = Depends(fetch_specific_user),
        service: OperationService = Depends()
):
    return service.get_specific_todo(user_id=user.id, todo_id=todo_id)


@router.post("/", response_model=TodoOperation)
def create_todo(
        operation_data: TodoOperationCreate,
        user: User = Depends(fetch_specific_user),
        service: OperationService = Depends()
):
    return service.create_todo(user_id=user.id, operation=operation_data)


@router.put("/{todo_id}", response_model=TodoOperation)
def update_todo(
        todo_id: int,
        operation_data: TodoOperationUpdate,
        user: User = Depends(fetch_specific_user),
        service: OperationService = Depends()
):
    return service.update_todo(
        todo_id=todo_id,
        operation=operation_data,
        user_id=user.id
    )


@router.delete("/{todo_id}")
def delete_todo(
        todo_id: int,
        user: User = Depends(fetch_specific_user),
        service: OperationService = Depends()
):
    service.delete_todo(user_id=user.id, todo_id=todo_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
