from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.endpoints import app
from db.database import Base

client = TestClient(app)

DUMMY_DB = "sqlite:///./test.db"

engine = create_engine(
    DUMMY_DB, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200