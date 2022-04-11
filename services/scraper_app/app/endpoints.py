from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from celery.result import AsyncResult

from computing.tasks import ScrappingTask
from app.auth.auth_bearer import JWTBearer

app = FastAPI()

"""
Allowlist only predefined HTTP requests.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8006"],
    allow_methods=["GET"],
    allow_headers=["Accept", "X-Requested-With", "X-CSRFToken", "Authorization"],
)

"""
Endpotint used for build testing
"""


@app.get("/", status_code=200)
def main_route() -> str:
    return "Ok!"


"""
Endpoint takes a keyword from consumer runs celery task and returns task_id.
Could be called only by authorized consumer with valid JWT.
"""


@app.get("/new_task/{keyword}", dependencies=[Depends(JWTBearer())], status_code=200)
def insert_task(keyword: str) -> JSONResponse:
    task = ScrappingTask().delay(keyword)

    return JSONResponse({"task_id": task.id})


"""
Takes a task_id and checks execution status.
If content is scraped returns content to frontend.
Endpoint could be called only by authorized consumer with valid JWT.
"""


@app.get("/tasks/{task_id}", dependencies=[Depends(JWTBearer())], status_code=200)
def check_task(task_id: str) -> JSONResponse:
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "content": task_result.result,
    }

    return JSONResponse(result)
