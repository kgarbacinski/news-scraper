from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from celery.result import AsyncResult

from computing.tasks import ScrappingTask
from app.auth.auth_bearer import JWTBearer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8006"],
    allow_methods=["GET"],
    allow_headers=["Accept", "X-Requested-With", "X-CSRFToken", "Authorization"],
    )

@app.get("/", status_code=200)
def main_route():
    return 'Ok!'    

@app.get("/new_task/{keyword}", dependencies=[Depends(JWTBearer())], status_code=200)
def insert_task(keyword: str):
    task = ScrappingTask().delay(keyword)
    
    return JSONResponse({"task_id": task.id})

@app.get("/tasks/{task_id}", dependencies=[Depends(JWTBearer())], status_code=200)
def check_task(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "content": task_result.result
    }

    return JSONResponse(result)