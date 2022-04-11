from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.endpoints import app, binding
from db.database import Base, get_db

DUMMY_DB = "sqlite:///./test.db"

engine = create_engine(
    DUMMY_DB, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

binding = Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_app_is_ready():
    response = client.get("/")
    assert response.status_code == 200