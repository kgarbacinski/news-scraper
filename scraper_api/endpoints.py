from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from pydantic import BaseModel

from computing.tasks import scraper_task

app = FastAPI()

# class Keyword(BaseModel):
#     keyword: str


# # @app.post("/tasks", status_code=201)
# # def run_task(keyword: Keyword):
# #     task = create_new_task.delay(keyword)
# #     return JSONResponse({"task_id": task.id})

@app.get("/new_task/{keyword}", status_code=201)
def run_task(keyword: str):
    task = scraper_task.delay(keyword)
    
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