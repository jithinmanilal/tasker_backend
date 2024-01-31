from typing import List
from datetime import date
from uuid import UUID
from app.models.user_model import User
from app.models.task_model import Task
from app.schemas.task_schemas import TaskCreate, TaskUpdate

class TaskService:
    @staticmethod
    async def list_all_tasks(user: User) -> List[Task]:
        tasks = await Task.find(Task.owner.id == user.id).to_list()
        return tasks
    
    @staticmethod
    async def list_tasks_by_date(user: User, date: date) -> List[Task]:
        tasks = await Task.find(Task.owner.id == user.id, Task.task_date == date).to_list()
        return tasks

    @staticmethod
    async def create_task(data: TaskCreate, user: User) -> Task:
        task = Task(**data.dict(), owner=user)
        return await task.insert()
    
    @staticmethod
    async def retrieve_task(current_user: User, task_id: UUID):
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == current_user.id)
        return task
    
    @staticmethod
    async def update_task(current_user: User, task_id: UUID, data: TaskUpdate):
        task = await TaskService.retrieve_task(current_user, task_id)
        await task.update({"$set": data.dict(exclude_unset=True)})
        await task.save()
        return task
    
    @staticmethod
    async def delete_task(current_user: User, task_id: UUID):
        task = await TaskService.retrieve_task(current_user, task_id)
        if task:
            await task.delete()
        return None