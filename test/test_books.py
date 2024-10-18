import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine
from app.models import Book, Author

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)