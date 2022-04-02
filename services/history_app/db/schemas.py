from pydantic import BaseModel

class Record(BaseModel):
    task_id: str
    keyword: str
    content: str
    timestamp: str

    class Config:
        orm_mode = True
