from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import os
from typing import List

from app.auth.auth_bearer import JWTBearer
from db import models, schemas
from db.database import get_db, engine

"""
Reads the current stage where app is running (prod or CI)
and switch DB connection from postgres to local db.
"""
if not config("APP_STAGE", os.environ["APP_STAGE"]) == "TESTING":
    models.Base.metadata.create_all(bind=engine)

app = FastAPI()

"""
Only allowlisted consumers are allowed
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8006", "http://localhost:8004"],
    allow_methods=["GET", "POST"],
    allow_headers=["Accept", "X-Requested-With", "X-CSRFToken", "Authorization"],
)


@app.get("/", status_code=200)
def main_route() -> str:
    """
    Used for CI build testing only
    """
    return "Ok!"


@app.post(
    "/new_record", response_model=schemas.Record, dependencies=[Depends(JWTBearer())]
)
def add_new_record(data: schemas.Record, db: Session = Depends(get_db)) -> JSONResponse:
    """
    Receives POST request from auhorized consumer (scraper-app) and adds metadata to DB.
    """
    new_record = models.Record(
        task_id=data.task_id,
        keyword=data.keyword,
        content=data.content,
        timestamp=data.timestamp,
    )

    db.add(new_record)
    db.commit()

    return JSONResponse({"status": "History updated!"})


@app.get("/records", dependencies=[Depends(JWTBearer())])
def get_records(db: Session = Depends(get_db)) -> List:
    """
    Receives GET from ui-app and returns all querying records.
    """
    all_records = db.query(models.Record).order_by(models.Record.timestamp.desc()).all()

    return all_records
