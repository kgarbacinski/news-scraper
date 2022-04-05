from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from celery.result import AsyncResult

from computing.tasks import ScrappingTask

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
    )

@app.get("/new_task/{keyword}", status_code=201)
def insert_task(keyword: str):
    task = ScrappingTask().delay(keyword)
    
    return JSONResponse({"task_id": task.id})

@app.get("/tasks/{task_id}", status_code=200)
def check_task(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "content": task_result.result
    }

    return JSONResponse(result)