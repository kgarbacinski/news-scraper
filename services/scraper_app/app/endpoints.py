from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from celery.result import AsyncResult
from decouple import config

from computing.tasks import ScrappingTask
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import generate_JWT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
    )

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

@app.get('/utils/auth_token/{login}/{password}', status_code=200)
def generate_token(login: str, password: str):
    if login == config('ADMIN_LOGIN') and password == config('ADMIN_PASSWORD'):
        return generate_JWT()
    else:
        return 'Incorrect admin credentials!'