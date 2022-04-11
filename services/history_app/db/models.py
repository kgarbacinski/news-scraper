from sqlalchemy import Column, Integer, String
from .database import Base


class Record(Base):
    __tablename__ = "History"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String)
    keyword = Column(String)
    content = Column(String)
    timestamp = Column(String)

    def __repr__(self):
        return f"Record(id={self.id}, task_id={self.task_id}, keyword={self.keyword}, content={self.content}, timestamp={self.timestamp})"
