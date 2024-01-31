from typing import List
from datetime import date
from fastapi import APIRouter, Depends
from app.schemas.task_schemas import TaskResponse
from app.models.user_model import User
from app.models.task_model import Task
from app.api.dependencies.user_dependencies import get_current_user
from app.services.task_service import TaskService
from app.schemas.task_schemas import TaskCreate, TaskResponse, TaskUpdate
from uuid import UUID

task_router = APIRouter()

@task_router.get('/', summary="Get all tasks of the user", response_model=List[TaskResponse])
async def task_list(current_user: User = Depends(get_current_user)):
    return await TaskService.list_all_tasks(current_user)

@task_router.get('/list/{task_date}', summary="Get tasks for a specific date", response_model=List[TaskResponse])
async def task_list_by_date(task_date: date, current_user: User = Depends(get_current_user)):
    return await TaskService.list_tasks_by_date(current_user, task_date)

@task_router.post('/create', summary="Create Task", response_model=Task)
async def create_task(data: TaskCreate, current_user: User = Depends(get_current_user)):
    return await TaskService.create_task(data, current_user)

@task_router.get('/{task_id}', summary="Get a task by task-id", response_model=TaskResponse)
async def retrieve(task_id: UUID, current_user: User = Depends(get_current_user)):
    return await TaskService.retrieve_task(current_user, task_id)

@task_router.put('/{task_id}', summary="Update task by id", response_model=TaskResponse)
async def update(task_id: UUID, data: TaskUpdate, current_user: User = Depends(get_current_user)):
    return await TaskService.update_task(current_user, task_id, data)

@task_router.delete('/{task_id}', summary="Delete task by id")
async def delete(task_id: UUID, current_user: User = Depends(get_current_user)):
    await TaskService.delete_task(current_user, task_id)
    return None