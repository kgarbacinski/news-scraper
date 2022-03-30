from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json

app = FastAPI()

class Record(BaseModel):
    task_id: str
    keyword: str
    content: str
    timestamp: str


@app.post("/new_record")
def add_new_record(record: Record):
    return JSONResponse({
        'task_id': record.task_id,
        'keyword': record.keyword,
        'content': json.loads(record.content),
        'timestamp': record.timestamp
    })

@app.get('/records')
def get_records():
    pass