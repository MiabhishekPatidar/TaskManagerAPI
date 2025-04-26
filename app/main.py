from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

API_KEY = "mysecretapikey123"  # Hardcoded for now

app = FastAPI()
from fastapi import Header, Depends

# Dependency to check API Key
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


# In-memory storage
tasks = []

# Pydantic Model
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# Home Route
@app.get("/", dependencies=[Depends(verify_api_key)])
def read_root():
    return {"message": "Hello, FastAPI World!"}

# Create Task
@app.post("/tasks/", response_model=Task, dependencies=[Depends(verify_api_key)])
def create_task(task: Task):
    tasks.append(task)
    return task

# Get All Tasks
@app.get("/tasks/", response_model=List[Task], dependencies=[Depends(verify_api_key)])
def get_tasks():
    return tasks

# Get Task by ID
@app.get("/tasks/{task_id}", response_model=Task, dependencies=[Depends(verify_api_key)])
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Update Task
@app.put("/tasks/{task_id}", response_model=Task, dependencies=[Depends(verify_api_key)])
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete Task
@app.delete("/tasks/{task_id}", dependencies=[Depends(verify_api_key)])
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

