from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult

from computing.tasks import ScrappingTask

app = FastAPI()


@app.get("/new_task/{keyword}", status_code=201)
def run_task(keyword: str):
    task = ScrappingTask().delay(keyword)
    return JSONResponse({"task_id": task.id})

@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }    
    return JSONResponse(result)