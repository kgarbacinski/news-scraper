from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.auth.auth_bearer import JWTBearer
from db import models, schemas
from db.database import get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8006", "http://localhost:8004"],
    allow_methods=["GET", "POST"],
    allow_headers=["Accept", "X-Requested-With", "X-CSRFToken", "Authorization"],
    )

@app.get("/", status_code=200)
def main_route():
    return 'Ok!'    

@app.post("/new_record", response_model=schemas.Record, dependencies=[Depends(JWTBearer())])
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

    
@app.get('/records', dependencies=[Depends(JWTBearer())])
def get_records(db: Session = Depends(get_db)):
    all_records = (
        db.query(models.Record)
        .order_by(models.Record.timestamp.desc())
        .all()
    )

    return all_records