from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db import models, schemas
from db.database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    )


@app.post("/new_record", response_model=schemas.Record)
def add_new_record(data: schemas.Record, db: Session = Depends(get_db)):
    new_record = models.Record(
        task_id = data.task_id, 
        keyword = data.keyword, 
        content = data.content, 
        timestamp = data.timestamp
    )

    db.add(new_record)
    db.commit()

    return JSONResponse({'status': 'History updated!'})

    
@app.get('/records')
def get_records(db: Session = Depends(get_db)):
    all_records = db.query(models.Record).all()

    return all_records