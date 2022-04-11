from pydantic import BaseModel


class Record(BaseModel):
    """
    Table schema
    """

    task_id: str
    keyword: str
    content: str
    timestamp: str

    class Config:
        orm_mode = True
