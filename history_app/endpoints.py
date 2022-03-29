from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Record(BaseModel):
    task_id: str
    keyword: str
    content: str

@app.get("/test")
def test():
    return JSONResponse({"test": "dupa"})

@app.post("/new_record/")
def add_new_record(record: Record):
    return record